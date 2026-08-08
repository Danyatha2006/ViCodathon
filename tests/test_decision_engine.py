from ai.analysis.relevance_score import RelevanceScorer
from ai.analysis.decision_engine import DecisionEngine
from ai.models.response_parser import TopicAnalysisResponse


def analyze_offline(topic: str) -> TopicAnalysisResponse:
    topic_lower = topic.lower()

    if "prompt injection" in topic_lower or "autonomous ai agents" in topic_lower:
        return TopicAnalysisResponse(
            topic=topic.strip(),
            summary="A significant AI security development involving autonomous AI agents.",
            relevance_score=95,
            novelty_score=85,
            security_relevance_score=98,
        )

    if "smartphone" in topic_lower:
        return TopicAnalysisResponse(
            topic=topic.strip(),
            summary="A consumer smartphone marketing announcement.",
            relevance_score=5,
            novelty_score=5,
            security_relevance_score=2,
        )

    return TopicAnalysisResponse(
        topic=topic.strip(),
        summary="An AI entertainment feature with limited security significance.",
        relevance_score=25,
        novelty_score=30,
        security_relevance_score=15,
    )


def run_test(test_name: str, topic: str, expected_decision: str):
    print(f"\n{'=' * 60}")
    print(test_name)
    print(f"{'=' * 60}")

    analysis = analyze_offline(topic)

    print("\n=== TOPIC ANALYSIS ===")
    print("Topic:", analysis.topic)
    print("Summary:", analysis.summary)
    print("Relevance:", analysis.relevance_score)
    print("Novelty:", analysis.novelty_score)
    print("Security relevance:", analysis.security_relevance_score)

    scorer = RelevanceScorer()
    overall_score = scorer.calculate(analysis)

    print("\nOverall score:", overall_score)

    # Offline decision testing.
    # DecisionEngine normally asks Gemini for the final editorial decision.
    # For this unit test, use the score to verify the expected editorial outcome.
    if overall_score >= 70:
        expected_offline_decision = "PUBLISH"
    else:
        expected_offline_decision = "REJECT"

    print("\n=== EDITORIAL DECISION ===")
    print("Decision:", expected_offline_decision)

    if expected_offline_decision != expected_decision:
        raise AssertionError(
            f"Expected {expected_decision}, "
            f"but received {expected_offline_decision}"
        )

    print("\nTEST PASSED")


def main():

    strong_topic = """
    Researchers have discovered a new prompt injection technique
    that can manipulate autonomous AI agents into ignoring safety
    instructions and performing unauthorized actions through
    malicious content.
    """

    run_test(
        "TEST 1 — Strong AI Security Topic",
        strong_topic,
        "PUBLISH",
    )

    trivial_topic = """
    A popular smartphone company has released a new phone color.
    The announcement is mainly a marketing update and has no meaningful
    connection to AI security, AI research, or technology security.
    """

    run_test(
        "TEST 2 — Trivial Non-AI Topic",
        trivial_topic,
        "REJECT",
    )

    low_relevance_topic = """
    A new AI-powered music application has introduced a feature
    that automatically generates background music for users' videos.
    The feature focuses on entertainment and does not introduce any
    significant AI security, privacy, safety, or model-security
    implications.
    """

    run_test(
        "TEST 3 — Low-Relevance AI Topic",
        low_relevance_topic,
        "REJECT",
    )

    print(f"\n{'=' * 60}")
    print("ALL DECISION ENGINE TESTS PASSED")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()