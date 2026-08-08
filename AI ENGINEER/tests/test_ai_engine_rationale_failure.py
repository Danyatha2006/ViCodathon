from ai.ai_engine import AIEngine
from ai.models.response_parser import (
    TopicAnalysisResponse,
    EditorialDecisionResponse,
    GeneratedPostResponse,
)


class FakeMemoryManager:
    """Fake memory manager for offline testing."""

    def __init__(self):
        self.saved_memory = None

    def get_relevant_memory(self, topic):
        return {
            "memory": "No previous relevant coverage."
        }

    def save_post_memory(self, memory_data):
        self.saved_memory = memory_data

    def close(self):
        pass


class FakeDuplicateChecker:
    """Simulates a genuinely new topic."""

    def check(self, topic):
        return {
            "is_duplicate": False,
            "similar_memory": "",
            "recommendation": "PUBLISH_NEW_TOPIC",
        }


class FakeAnalyzer:
    """Offline topic analyzer."""

    def analyze(self, topic):
        return TopicAnalysisResponse(
            topic=topic,
            summary=(
                "A significant AI security technique "
                "affecting autonomous AI agents."
            ),
            relevance_score=95,
            novelty_score=90,
            security_relevance_score=98,
        )


class FakeScorer:
    """Offline relevance scorer."""

    def calculate(self, analysis):
        return 94.45


class FakeDecisionEngine:
    """Offline editorial decision engine."""

    def decide(self, analysis, overall_score):
        return EditorialDecisionResponse(
            decision="PUBLISH",
            reason="Highly relevant AI security topic.",
        )


class FakeContentGenerator:
    """Simulates successful content generation."""

    def generate(self, *args, **kwargs):
        return GeneratedPostResponse(
            post=(
                "A new AI security technique demonstrates "
                "how runtime monitoring can detect suspicious "
                "behavior in autonomous AI agents."
            )
        )


class FailingRationaleGenerator:
    """Simulates rationale generation failure."""

    def generate(self, *args, **kwargs):
        raise RuntimeError(
            "Simulated rationale generation failure"
        )


def main():

    print("\n" + "=" * 70)
    print("PHASE 10.8 — RATIONALE FAILURE SAFETY TEST")
    print("=" * 70)

    topic = (
        "A new runtime monitoring technique detects "
        "suspicious behavior in autonomous AI agents."
    )

    print("\nTesting topic:")
    print(topic)

    engine = AIEngine()

    # Replace external dependencies with offline test doubles.
    fake_memory = FakeMemoryManager()

    engine.memory_manager = fake_memory
    engine.duplicate_checker = FakeDuplicateChecker()

    engine.analyzer = FakeAnalyzer()
    engine.scorer = FakeScorer()
    engine.decision_engine = FakeDecisionEngine()

    # Content generation succeeds.
    engine.content_generator = FakeContentGenerator()

    # Rationale generation deliberately fails.
    engine.rationale_generator = FailingRationaleGenerator()

    print("\nRunning offline pipeline...")

    try:

        engine.process_topic(topic)

    except RuntimeError as exc:

        print("\nExpected error caught:")
        print(exc)

        # A failed rationale means the complete publish
        # operation did not finish successfully.
        assert fake_memory.saved_memory is None, (
            "Incomplete post must NOT be saved "
            "to memory."
        )

        print(
            "\nFailed rationale was NOT "
            "saved to memory."
        )

        engine.close()

        print("\n" + "=" * 70)
        print(
            "PHASE 10.8 RATIONALE FAILURE "
            "SAFETY TEST PASSED"
        )
        print("=" * 70)

        return

    raise AssertionError(
        "Rationale generation failure should "
        "have raised RuntimeError."
    )


if __name__ == "__main__":
    main()