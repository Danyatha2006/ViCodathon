from ai.ai_engine import AIEngine


class FakeAnalysis:
    def __init__(self, topic):
        self.topic = topic
        self.summary = "Promotional smartphone color announcement."
        self.relevance_score = 0
        self.novelty_score = 5
        self.security_relevance_score = 0


class FakeAnalyzer:
    def analyze(self, topic):
        return FakeAnalysis(topic)


class FakeDecision:
    decision = "REJECT"
    reason = "Topic is not relevant to AURA."


class FakeDecisionEngine:
    def decide(self, analysis, overall_score):
        return FakeDecision()


def main():
    print("\n" + "=" * 70)
    print("PHASE 10.6 — OFFLINE REJECTION SAFETY TEST")
    print("=" * 70)

    topic = "A smartphone company announced a new phone color."

    print("\nTesting weak topic:")
    print(topic)

    engine = AIEngine()

    # Completely replace the Gemini-dependent analyzer.
    engine.analyzer = FakeAnalyzer()

    # Replace editorial decision with an offline decision.
    engine.decision_engine = FakeDecisionEngine()

    # Prevent Breeth calls.
    engine.memory_manager.get_relevant_memory = lambda topic: None

    engine.duplicate_checker.check = lambda topic: {
        "is_duplicate": False,
        "similar_memory": "",
        "recommendation": "NEW_TOPIC",
    }

    print("\nRunning offline pipeline...")

    result = engine.process_topic(topic)

    print("\n=== RESULT ===")
    print("Status:", result["status"])
    print("Reason:", result["reason"])
    print("Decision:", result["decision"].decision)

    if result["status"] != "REJECTED":
        raise AssertionError(
            "Weak topic should have been rejected."
        )

    if result["reason"] != "EDITORIAL_DECISION":
        raise AssertionError(
            "Expected editorial decision rejection."
        )

    if "generated_post" in result:
        raise AssertionError(
            "Rejected topic must not contain generated_post."
        )

    if "rationale" in result:
        raise AssertionError(
            "Rejected topic must not contain rationale."
        )

    engine.close()

    print("\nContent generation correctly skipped.")
    print("Rationale generation correctly skipped.")

    print("\n" + "=" * 70)
    print("PHASE 10.6 OFFLINE REJECTION TEST PASSED")
    print("=" * 70)


if __name__ == "__main__":
    main()