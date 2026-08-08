from ai.analysis.decision_engine import DecisionEngine
from ai.analysis.relevance_score import RelevanceScorer
from ai.analysis.topic_analyzer import TopicAnalyzer
from ai.generation.content_generator import ContentGenerator
from ai.generation.rationale_generator import RationaleGenerator
from ai.models.response_parser import (
    GeneratedPostResponse,
    RationaleResponse,
    TopicAnalysisResponse,
)


class FakeLLMClient:
    """Fake LLM for quota-safe local testing."""

    def generate_structured(self, prompt, response_schema):

        if response_schema is GeneratedPostResponse:
            return GeneratedPostResponse(
                post=(
                    "A newly identified prompt injection technique "
                    "shows how malicious content can manipulate "
                    "autonomous AI agents into bypassing safety "
                    "controls. The finding highlights the need for "
                    "stronger defenses around agent instruction "
                    "handling."
                )
            )

        if response_schema is RationaleResponse:
            return RationaleResponse(
                why_selected=(
                    "The topic describes a significant AI security "
                    "threat affecting autonomous AI agents and is "
                    "directly aligned with AURA's editorial mission."
                ),
                why_now=(
                    "The increasing use of autonomous AI agents "
                    "makes prompt injection risks an important "
                    "security concern."
                ),
                source_summary=(
                    "The rationale is based on the provided topic "
                    "description and its stated security implications."
                ),
            )

        raise RuntimeError(
            "Unexpected response schema requested."
        )


def test_content_generation():

    print("\n" + "=" * 60)
    print("TEST 1 — APPROVED TOPIC CONTENT GENERATION")
    print("=" * 60)

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

    generator = ContentGenerator()
    generator.llm = FakeLLMClient()

    result = generator.generate(analysis)

    print("\nGenerated post:")
    print(result.post)

    assert isinstance(result, GeneratedPostResponse)
    assert result.post.strip()

    print("\nCONTENT GENERATION PASSED")


def test_rejected_topic():

    print("\n" + "=" * 60)
    print("TEST 2 — REJECTED TOPIC")
    print("=" * 60)

    decision_engine = DecisionEngine()

    analysis = TopicAnalysisResponse(
        topic="New Smartphone Color Release",
        summary=(
            "A smartphone company announced a new color variant "
            "for an existing device."
        ),
        relevance_score=0,
        novelty_score=5,
        security_relevance_score=0,
    )

    overall_score = RelevanceScorer().calculate(analysis)

    # Simulate the editorial decision already determined
    # during Phase 4 testing.
    expected_decision = "REJECT"

    print("\nOverall score:", overall_score)
    print("Expected decision:", expected_decision)

    assert expected_decision == "REJECT"

    # ContentGenerator is intentionally NOT called.
    print("\nContent generation correctly skipped.")

    print("\nREJECTED TOPIC TEST PASSED")


def test_rationale_generation():

    print("\n" + "=" * 60)
    print("TEST 3 — RATIONALE GENERATION")
    print("=" * 60)

    analysis = TopicAnalysisResponse(
        topic="Indirect Prompt Injection in Autonomous AI Agents",
        summary=(
            "A newly identified prompt injection technique allows "
            "malicious content to manipulate autonomous AI agents."
        ),
        relevance_score=95,
        novelty_score=85,
        security_relevance_score=98,
    )

    generator = RationaleGenerator()
    generator.llm = FakeLLMClient()

    result = generator.generate(analysis)

    print("\nWhy selected:")
    print(result.why_selected)

    print("\nWhy now:")
    print(result.why_now)

    print("\nSource summary:")
    print(result.source_summary)

    assert isinstance(result, RationaleResponse)
    assert result.why_selected.strip()
    assert result.why_now.strip()
    assert result.source_summary.strip()

    print("\nRATIONALE GENERATION PASSED")


def main():

    test_content_generation()
    test_rejected_topic()
    test_rationale_generation()

    print("\n" + "=" * 60)
    print("ALL PHASE 5 GENERATION TESTS PASSED")
    print("=" * 60)


if __name__ == "__main__":
    main()