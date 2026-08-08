from ai.analysis.topic_analyzer import TopicAnalyzer


def main():
    analyzer = TopicAnalyzer()

    topic = (
        "Researchers discovered a new prompt injection "
        "technique that can manipulate AI agents into "
        "following malicious instructions."
    )

    result = analyzer.analyze(topic)

    print("\nTOPIC ANALYSIS")
    print("==============")
    print(f"Topic: {result.topic}")
    print(f"Summary: {result.summary}")
    print(f"Relevance: {result.relevance_score}")
    print(f"Novelty: {result.novelty_score}")
    print(
        f"Security relevance: "
        f"{result.security_relevance_score}"
    )


if __name__ == "__main__":
    main()