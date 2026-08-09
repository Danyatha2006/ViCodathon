from ai.ai_engine import AIEngine
from ai.models.response_parser import (
    TopicAnalysisResponse,
    EditorialDecisionResponse,
)


class FakeMemoryManager:

    def __init__(self):
        self.saved_memory = None

    def get_relevant_memory(self, topic):
        return {
            "memory": "No previous coverage."
        }

    def save_post_memory(self, memory_data):
        self.saved_memory = memory_data

    def close(self):
        pass


class FakeDuplicateChecker:

    def check(self, topic):
        return {
            "is_duplicate": False,
            "similar_memory": "",
            "recommendation": "PUBLISH_NEW_TOPIC",
        }


class FakeAnalyzer:

    def analyze(self, topic):
        return TopicAnalysisResponse(
            topic=topic,
            summary="Important AI security development.",
            relevance_score=95,
            novelty_score=90,
            security_relevance_score=98,
        )


class FakeScorer:

    def calculate(self, analysis):
        return 94.45


class FakeDecisionEngine:

    def decide(self, analysis, overall_score):
        return EditorialDecisionResponse(
            decision="PUBLISH",
            reason="Highly relevant AI security topic.",
        )


class FailingContentGenerator:

    def generate(self, *args, **kwargs):
        raise RuntimeError(
            "Simulated content generation failure"
        )


def main():

    print("\n" + "=" * 60)
    print("PHASE 7.5 — GENERATION FAILURE TEST")
    print("=" * 60)

    topic = (
        "A new security defense technique "
        "for autonomous AI agents."
    )

    engine = AIEngine()

    fake_memory = FakeMemoryManager()

    engine.memory_manager = fake_memory
    engine.duplicate_checker = FakeDuplicateChecker()

    engine.analyzer = FakeAnalyzer()
    engine.scorer = FakeScorer()
    engine.decision_engine = FakeDecisionEngine()

    engine.content_generator = FailingContentGenerator()

    print("\nProcessing topic...")
    print("Topic:", topic)

    try:

        engine.process_topic(topic)

    except RuntimeError as exc:

        print("\nExpected error caught:")
        print(exc)

        assert (
            fake_memory.saved_memory is None
        )

        print(
            "\nFailed generation was NOT "
            "saved to memory."
        )

        print("\n" + "=" * 60)
        print("PHASE 7.5 FAILURE TEST PASSED")
        print("=" * 60)

        return

    raise AssertionError(
        "Generation failure should have "
        "raised RuntimeError."
    )


if __name__ == "__main__":
    main()