from ai.generation.rationale_generator import RationaleGenerator
from ai.models.response_parser import (
    TopicAnalysisResponse,
    RationaleResponse,
)


class FakeLLMClient:
    """Fake LLM used for local testing without Gemini quota."""

    def generate_structured(self, prompt, response_schema):
        if response_schema is RationaleResponse:
            return RationaleResponse(
                why_selected=(
                    "The topic describes a significant AI security "
                    "threat affecting autonomous AI agents and is "
                    "directly aligned with AURA's editorial mission."
                ),
                why_now=(
                    "Autonomous AI agents are increasingly being used "
                    "in systems that can perform actions, making "
                    "prompt injection risks particularly important."
                ),
                source_summary=(
                    "The rationale is based on the provided topic "
                    "description and its reported security implications."
                ),
            )

        raise RuntimeError(
            "Unexpected response schema requested by the test."
        )


def main():

    print("\n=== RATIONALE GENERATOR LOCAL TEST ===")

    analysis = TopicAnalysisResponse(
        topic="Indirect Prompt Injection in Autonomous AI Agents",
        summary=(
            "A newly identified prompt injection technique allows "
            "malicious content to manipulate autonomous AI agents "
            "into overriding safety instructions."
        ),
        relevance_score=95,
        novelty_score=85,
        security_relevance_score=98,
    )

    generator = RationaleGenerator()

    # Replace the real Gemini client only for this local test.
    generator.llm = FakeLLMClient()

    print("\nGenerating rationale...")

    result = generator.generate(analysis)

    print("\n=== RATIONALE ===")
    print("Why selected:", result.why_selected)
    print("Why now:", result.why_now)
    print("Source summary:", result.source_summary)

    if not result.why_selected.strip():
        raise AssertionError("why_selected is empty.")

    if not result.why_now.strip():
        raise AssertionError("why_now is empty.")

    if not result.source_summary.strip():
        raise AssertionError("source_summary is empty.")

    if not isinstance(result, RationaleResponse):
        raise AssertionError(
            "Generator did not return RationaleResponse."
        )

    print("\nRATIONALE GENERATION TEST PASSED")


if __name__ == "__main__":
    main()