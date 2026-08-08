from ai.ai_engine import AIEngine
from ai.models.response_parser import (
    TopicAnalysisResponse,
    EditorialDecisionResponse,
)


class FakeMemoryManager:
    """Fake memory manager so this test does not use Breeth."""

    def get_relevant_memory(self, topic):
        return {
            "memory": "No previous relevant coverage."
        }

    def save_post_memory(self, memory_data):
        raise AssertionError(
            "Rejected topic must NOT be saved to memory."
        )

    def close(self):
        pass


class FakeDuplicateChecker:
    """Fake duplicate checker for a new topic."""

    def check(self, topic):
        return {
            "is_duplicate": False,
            "similar_memory": "",
            "recommendation": "PUBLISH_NEW_TOPIC",
        }


class FakeAnalyzer:
    """Fake analyzer so Gemini is not called."""

    def analyze(self, topic):
        return TopicAnalysisResponse(
            topic=topic,
            summary="A trivial promotional announcement.",
            relevance_score=5,
            novelty_score=10,
            security_relevance_score=0,
        )


class FakeScorer:

    def calculate(self, analysis):
        return 4.25


class FakeDecisionEngine:
    """Fake editorial engine that rejects the weak topic."""

    def decide(self, analysis, overall_score):
        return EditorialDecisionResponse(
            decision="REJECT",
            reason=(
                "The topic has insufficient relevance "
                "and security significance for AURA."
            ),
        )


class FakeContentGenerator:

    def generate(self, *args, **kwargs):
        raise AssertionError(
            "Content generation must NOT run "
            "for a rejected topic."
        )


class FakeRationaleGenerator:

    def generate(self, *args, **kwargs):
        raise AssertionError(
            "Rationale generation must NOT run "
            "for a rejected topic."
        )


def main():

    print("\n" + "=" * 60)
    print("PHASE 7.2 — AI ENGINE REJECT TEST")
    print("=" * 60)

    topic = (
        "A smartphone company announced "
        "a new phone color."
    )

    engine = AIEngine()

    # Replace real components with controlled test doubles.
    engine.memory_manager = FakeMemoryManager()
    engine.duplicate_checker = FakeDuplicateChecker()

    engine.analyzer = FakeAnalyzer()
    engine.scorer = FakeScorer()
    engine.decision_engine = FakeDecisionEngine()

    engine.content_generator = FakeContentGenerator()
    engine.rationale_generator = FakeRationaleGenerator()

    print("\nProcessing weak topic...")
    print("Topic:", topic)

    result = engine.process_topic(topic)

    print("\n=== AI ENGINE RESULT ===")
    print("Status:", result["status"])
    print("Reason:", result["reason"])
    print(
        "Decision:",
        result["decision"].decision,
    )
    print(
        "Overall score:",
        result["overall_score"],
    )

    assert result["status"] == "REJECTED"

    assert result["reason"] == (
        "EDITORIAL_DECISION"
    )

    assert (
        result["decision"].decision
        == "REJECT"
    )

    assert "generated_post" not in result

    assert "rationale" not in result

    print("\nContent generation correctly skipped.")
    print("Rationale generation correctly skipped.")

    print("\n" + "=" * 60)
    print("PHASE 7.2 REJECT TEST PASSED")
    print("=" * 60)


if __name__ == "__main__":
    main()