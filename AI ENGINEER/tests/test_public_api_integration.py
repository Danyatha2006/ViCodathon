from ai.public_api import process_topic
from ai.ai_engine import AIEngine
from ai.models.response_parser import (
    TopicAnalysisResponse,
    EditorialDecisionResponse,
)


class FakeMemoryManager:

    def get_relevant_memory(self, topic):
        return {"memory": "No previous coverage."}

    def save_post_memory(self, memory_data):
        raise AssertionError(
            "Rejected topic must not be saved."
        )

    def close(self):
        pass


class FakeDuplicateChecker:

    def check(self, topic):
        return {
            "is_duplicate": False,
            "similar_memory": "",
            "recommendation": "NEW_TOPIC",
        }


class FakeAnalyzer:

    def analyze(self, topic):
        return TopicAnalysisResponse(
            topic=topic,
            summary="Trivial promotional announcement.",
            relevance_score=5,
            novelty_score=10,
            security_relevance_score=0,
        )


class FakeScorer:

    def calculate(self, analysis):
        return 4.25


class FakeDecisionEngine:

    def decide(self, analysis, overall_score):
        return EditorialDecisionResponse(
            decision="REJECT",
            reason="Insufficient relevance.",
        )


def main():

    print("\n" + "=" * 60)
    print("STEP 5 — PUBLIC API OFFLINE INTEGRATION TEST")
    print("=" * 60)

    # Verify the wrapper points to the real engine.
    original_process = process_topic

    # Access the engine created by the wrapper indirectly
    # by temporarily replacing AIEngine.process_topic.
    original_process_topic = AIEngine.process_topic

    def fake_process(self, topic):
        self.memory_manager = FakeMemoryManager()
        self.duplicate_checker = FakeDuplicateChecker()
        self.analyzer = FakeAnalyzer()
        self.scorer = FakeScorer()
        self.decision_engine = FakeDecisionEngine()

        return original_process_topic(self, topic)

    AIEngine.process_topic = fake_process

    try:

        topic = "A smartphone company announced a new phone color."

        print("\nProcessing:")
        print(topic)

        result = original_process(topic)

        print("\nStatus:", result["status"])
        print("Reason:", result["reason"])
        print("Decision:", result["decision"].decision)

        assert result["status"] == "REJECTED"
        assert result["reason"] == "EDITORIAL_DECISION"
        assert result["decision"].decision == "REJECT"

        assert "generated_post" not in result
        assert "rationale" not in result

        print("\n✓ Public API reached AIEngine")
        print("✓ Offline rejection worked")
        print("✓ Content generation skipped")
        print("✓ Rationale generation skipped")

    finally:
        AIEngine.process_topic = original_process_topic

    print("\n" + "=" * 60)
    print("STEP 5 PUBLIC API INTEGRATION TEST PASSED")
    print("=" * 60)


if __name__ == "__main__":
    main()