import json
import os
from typing import Optional, Type, TypeVar

import requests
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel

load_dotenv(override=False)

T = TypeVar("T", bound=BaseModel)


class LLMClient:
    """Centralized LLM client with Gemini -> OpenRouter fallback."""

    DEFAULT_MODEL = "gemini-3.6-flash"
    OPENROUTER_MODEL = "openai/gpt-4o-mini"

    def __init__(self, model: Optional[str] = None):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
        self.provider = os.getenv("LLM_PROVIDER", "auto").lower()

        if not self.api_key and not self.openrouter_api_key:
            raise RuntimeError(
                "Neither GEMINI_API_KEY nor OPENROUTER_API_KEY is configured."
            )

        self.model = model or self.DEFAULT_MODEL

        self.client = None

        # Normal mode: Gemini is the primary provider.
        # OpenRouter-only mode: Gemini is intentionally skipped.
        if self.api_key and self.provider != "openrouter":
            self.client = genai.Client(
                api_key=self.api_key
            )

    def _gemini_failed(self, exc: Exception) -> bool:
        """Return True when Gemini should trigger the fallback."""

        message = str(exc).upper()

        return any(
            indicator in message
            for indicator in (
                "429",
                "RESOURCE_EXHAUSTED",
                "QUOTA",
                "RATE LIMIT",
                "RATE_LIMIT",
                "TOO MANY REQUESTS",
            )
        )

    def _openrouter_generate(self, prompt: str) -> str:
        """Generate a normal text response using OpenRouter."""

        if not self.openrouter_api_key:
            raise RuntimeError(
                "OPENROUTER_API_KEY is not configured."
            )

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {self.openrouter_api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": self.OPENROUTER_MODEL,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
            },
            timeout=60,
        )

        response.raise_for_status()

        data = response.json()

        text = data["choices"][0]["message"]["content"]

        if not text or not text.strip():
            raise RuntimeError(
                "OpenRouter returned an empty response."
            )

        return text.strip()

    def _openrouter_structured(
        self,
        prompt: str,
        response_schema: Type[T],
    ) -> T:
        """Generate and validate a structured response using OpenRouter."""

        if not self.openrouter_api_key:
            raise RuntimeError(
                "OPENROUTER_API_KEY is not configured."
            )

        schema = response_schema.model_json_schema()

        structured_prompt = f"""
{prompt}

Return ONLY valid JSON matching this schema:

{json.dumps(schema, indent=2)}
"""

        text = self._openrouter_generate(
            structured_prompt
        )

        try:
            return response_schema.model_validate_json(
                text
            )

        except Exception:
            # Some models may wrap JSON in markdown fences.
            cleaned = text.strip()

            if cleaned.startswith("```json"):
                cleaned = cleaned[len("```json"):].strip()

            if cleaned.startswith("```"):
                cleaned = cleaned[len("```"):].strip()

            if cleaned.endswith("```"):
                cleaned = cleaned[:-3].strip()

            return response_schema.model_validate_json(
                cleaned
            )

    def generate(self, prompt: str) -> str:
        """Generate text using Gemini, falling back to OpenRouter."""

        if not prompt or not prompt.strip():
            raise ValueError("Prompt cannot be empty.")

        # --------------------------------------------------
        # OPENROUTER-ONLY TEST MODE
        # --------------------------------------------------

        if self.provider == "openrouter":
            return self._openrouter_generate(prompt)

        # --------------------------------------------------
        # NORMAL MODE: GEMINI FIRST
        # --------------------------------------------------

        if self.client:
            try:
                response = self.client.models.generate_content(
                    model=self.model,
                    contents=prompt,
                )

                if response is None:
                    raise RuntimeError(
                        "Gemini returned no response."
                    )

                text = response.text

                if not text or not text.strip():
                    raise RuntimeError(
                        "Gemini returned an empty response."
                    )

                return text.strip()

            except Exception as exc:

                # Only quota/rate-limit failures trigger fallback.
                if not self._gemini_failed(exc):
                    raise

                print(
                    "Gemini quota/API limit reached. "
                    "Switching to OpenRouter..."
                )

        # --------------------------------------------------
        # FALLBACK
        # --------------------------------------------------

        return self._openrouter_generate(prompt)

    def generate_structured(
        self,
        prompt: str,
        response_schema: Type[T],
    ) -> T:
        """Generate structured data using Gemini, then OpenRouter."""

        if not prompt or not prompt.strip():
            raise ValueError("Prompt cannot be empty.")

        if not response_schema:
            raise ValueError("Response schema is required.")

        # --------------------------------------------------
        # OPENROUTER-ONLY TEST MODE
        # --------------------------------------------------

        if self.provider == "openrouter":
            return self._openrouter_structured(
                prompt,
                response_schema,
            )

        # --------------------------------------------------
        # NORMAL MODE: GEMINI FIRST
        # --------------------------------------------------

        if self.client:
            try:
                response = self.client.models.generate_content(
                    model=self.model,
                    contents=prompt,
                    config={
                        "response_mime_type": "application/json",
                        "response_schema": response_schema,
                    },
                )

                if response is None:
                    raise RuntimeError(
                        "Gemini returned no response."
                    )

                if response.parsed is not None:
                    return response.parsed

                if not response.text:
                    raise RuntimeError(
                        "Gemini returned an empty structured response."
                    )

                return response_schema.model_validate_json(
                    response.text
                )

            except Exception as exc:

                # Only quota/rate-limit failures trigger fallback.
                if not self._gemini_failed(exc):
                    raise

                print(
                    "Gemini quota/API limit reached. "
                    "Switching to OpenRouter..."
                )

        # --------------------------------------------------
        # FALLBACK
        # --------------------------------------------------

        return self._openrouter_structured(
            prompt,
            response_schema,
        )