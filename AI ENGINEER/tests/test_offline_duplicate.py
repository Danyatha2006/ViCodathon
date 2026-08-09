from ai.ai_engine import AIEngine


class FakeAnalysis:
    def __init__(self, topic):
        self.topic = topic
        self.summary = "Previously covered AI security topic."
        self.relevance_score = 95
        self.novelty_score = 80
        self.security_relevance_score = 98


class FakeAnalyzer:
    def analyze(self, topic):
        return FakeAnalysis(topic)


def main():
    print("\n" + "=" * 70)
    print("PHASE 10.7 — OFFLINE DUPLICATE SAFETY TEST")
    print("=" * 70)

    topic = "Indirect Prompt Injection in Autonomous AI Agents"

    print("\nTesting duplicate topic:")
    print(topic)

    engine = AIEngine()

    # No Gemini
    engine.analyzer = FakeAnalyzer()

    # No Breeth
    engine.memory_manager.get_relevant_memory = lambda topic: None

    # Simulate an already stored topic
    engine.duplicate_checker.check = lambda topic: {
        "is_duplicate": True,
        "similar_memory": (
            "Indirect Prompt Injection in Autonomous AI Agents"
        ),
        "recommendation": "REJECT_DUPLICATE",
    }

    print("\nRunning offline pipeline...")

    result = engine.process_topic(topic)

    print("\n=== RESULT ===")
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

    if result["status"] != "REJECTED":
        raise AssertionError(
            "Duplicate topic should have been rejected."
        )

    if result["reason"] != "DUPLICATE":
        raise AssertionError(
            "Expected duplicate rejection."
        )

    if not result["duplicate_check"]["is_duplicate"]:
        raise AssertionError(
            "Topic should be detected as duplicate."
        )

    if "generated_post" in result:
        raise AssertionError(
            "Duplicate topic must not generate content."
        )

    if "rationale" in result:
        raise AssertionError(
            "Duplicate topic must not generate rationale."
        )

    engine.close()

    print("\nDuplicate correctly rejected.")
    print("Content generation correctly skipped.")
    print("Rationale generation correctly skipped.")

    print("\n" + "=" * 70)
    print("PHASE 10.7 OFFLINE DUPLICATE TEST PASSED")
    print("=" * 70)


if __name__ == "__main__":
    main()