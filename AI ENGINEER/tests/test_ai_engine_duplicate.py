from ai.ai_engine import AIEngine
from ai.models.response_parser import (
    TopicAnalysisResponse,
)


class FakeMemoryManager:
    """Fake memory manager for duplicate testing."""

    def get_relevant_memory(self, topic):
        return {
            "memory": (
                "AURA previously covered indirect "
                "prompt injection in autonomous AI agents."
            )
        }

    def save_post_memory(self, memory_data):
        raise AssertionError(
            "Duplicate topic must NOT be saved."
        )

    def close(self):
        pass


class FakeDuplicateChecker:
    """Simulates detection of an exact duplicate."""

    def check(self, topic):
        return {
            "is_duplicate": True,
            "similar_memory": (
                "Indirect Prompt Injection in "
                "Autonomous AI Agents is an exploit "
                "technique that bypasses safety controls."
            ),
            "recommendation": "REJECT_DUPLICATE",
        }


class FakeAnalyzer:
    """Fake analyzer to avoid Gemini."""

    def analyze(self, topic):
        return TopicAnalysisResponse(
            topic=topic,
            summary=(
                "A prompt injection technique "
                "targeting autonomous AI agents."
            ),
            relevance_score=95,
            novelty_score=80,
            security_relevance_score=98,
        )


class FakeScorer:

    def calculate(self, analysis):
        return 92.45


class FakeContentGenerator:

    def generate(self, *args, **kwargs):
        raise AssertionError(
            "Content generation must NOT run "
            "for a duplicate."
        )


class FakeRationaleGenerator:

    def generate(self, *args, **kwargs):
        raise AssertionError(
            "Rationale generation must NOT run "
            "for a duplicate."
        )


def main():

    print("\n" + "=" * 60)
    print("PHASE 7.3 — AI ENGINE DUPLICATE TEST")
    print("=" * 60)

    topic = (
        "Indirect Prompt Injection in "
        "Autonomous AI Agents"
    )

    engine = AIEngine()

    # Replace real external components with test doubles.
    engine.memory_manager = FakeMemoryManager()
    engine.duplicate_checker = FakeDuplicateChecker()

    engine.analyzer = FakeAnalyzer()
    engine.scorer = FakeScorer()

    engine.content_generator = FakeContentGenerator()
    engine.rationale_generator = FakeRationaleGenerator()

    print("\nProcessing duplicate topic...")
    print("Topic:", topic)

    result = engine.process_topic(topic)

    print("\n=== AI ENGINE RESULT ===")

    print("Status:", result["status"])
    print("Reason:", result["reason"])
    print(
        "Duplicate:",
        result["duplicate_check"]["is_duplicate"],
    )
    print(
        "Recommendation:",
        result["duplicate_check"]["recommendation"],
    )

    assert result["status"] == "REJECTED"

    assert result["reason"] == "DUPLICATE"

    assert (
        result["duplicate_check"]["is_duplicate"]
        is True
    )

    assert (
        result["duplicate_check"]["recommendation"]
        == "REJECT_DUPLICATE"
    )

    assert "generated_post" not in result

    assert "rationale" not in result

    print("\nDuplicate correctly rejected.")

    print("Content generation correctly skipped.")
    print("Rationale generation correctly skipped.")

    print("\n" + "=" * 60)
    print("PHASE 7.3 DUPLICATE TEST PASSED")
    print("=" * 60)


if __name__ == "__main__":
    main()