from ai.models.llm_client import LLMClient
from ai.models.response_parser import (
    TopicAnalysisResponse,
    RationaleResponse,
)
from ai.persona.persona import AURAPersona


class RationaleGenerator:
    """Generates the editorial rationale for a selected topic."""

    def __init__(self):
        self.llm = LLMClient()
        self.persona = AURAPersona()

    def generate(
        self,
        analysis: TopicAnalysisResponse,
    ) -> RationaleResponse:
        """Generate a structured explanation for selecting a topic."""

        if not analysis:
            raise ValueError("Topic analysis is required.")

        prompt = f"""
{self.persona.get_system_prompt()}

TASK

Explain why AURA selected the following topic for publication.

TOPIC

{analysis.topic}

SUMMARY

{analysis.summary}

RELEVANCE SCORE

{analysis.relevance_score}/100

NOVELTY SCORE

{analysis.novelty_score}/100

SECURITY RELEVANCE SCORE

{analysis.security_relevance_score}/100

Provide an editorial rationale covering:

1. Why this topic was selected.
2. Why it matters now.
3. What makes the topic relevant to AURA's audience.

Rules:

- Be concise.
- Be analytical.
- Be evidence-driven.
- Do not invent facts.
- Do not exaggerate.
- Do not use promotional language.
- Base the rationale only on the provided topic and analysis.
- Maintain AURA's editorial voice.

Return the result using the required structured format.
"""

        result = self.llm.generate_structured(
            prompt,
            RationaleResponse,
        )

        if not result.why_selected.strip():
            raise RuntimeError(
                "Rationale generator returned an empty selection reason."
            )

        if not result.why_now.strip():
            raise RuntimeError(
                "Rationale generator returned an empty why-now explanation."
            )

        if not result.source_summary.strip():
            raise RuntimeError(
                "Rationale generator returned an empty source summary."
            )

        return result