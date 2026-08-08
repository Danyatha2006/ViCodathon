import os
from typing import Optional, Type, TypeVar

from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel

load_dotenv()

T = TypeVar("T", bound=BaseModel)


class LLMClient:
    """Centralized Gemini client used by the AURA AI Engine."""

    DEFAULT_MODEL = "gemini-3.6-flash"

    def __init__(self, model: Optional[str] = None):
        self.api_key = os.getenv("GEMINI_API_KEY")

        if not self.api_key:
            raise RuntimeError(
                "GEMINI_API_KEY is not configured. "
                "Add it to the .env file."
            )

        self.model = model or self.DEFAULT_MODEL

        self.client = genai.Client(
            api_key=self.api_key
        )

    def generate(self, prompt: str) -> str:
        """Generate a normal text response."""

        if not prompt or not prompt.strip():
            raise ValueError("Prompt cannot be empty.")

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
        )

        if response is None:
            raise RuntimeError("Gemini returned no response.")

        text = response.text

        if not text or not text.strip():
            raise RuntimeError(
                "Gemini returned an empty response."
            )

        return text.strip()

    def generate_structured(
        self,
        prompt: str,
        response_schema: Type[T],
    ) -> T:
        """Generate a structured Pydantic response."""

        if not prompt or not prompt.strip():
            raise ValueError("Prompt cannot be empty.")

        if not response_schema:
            raise ValueError("Response schema is required.")

        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
                config={
                    "response_mime_type": "application/json",
                    "response_schema": response_schema,
                },
            )

        except Exception as exc:
            message = str(exc)

            if "429" in message or "RESOURCE_EXHAUSTED" in message:
                raise RuntimeError(
                    "Gemini API quota exhausted. "
                    "Use offline/fake LLM tests or wait for quota reset."
                ) from exc

            raise

        if response is None:
            raise RuntimeError("Gemini returned no response.")

        if response.parsed is not None:
            return response.parsed

        if not response.text:
            raise RuntimeError(
                "Gemini returned an empty structured response."
            )

        try:
            return response_schema.model_validate_json(
                response.text
            )
        except Exception as exc:
            raise RuntimeError(
                "Gemini returned data that could not be "
                "validated against the requested schema."
            ) from exc