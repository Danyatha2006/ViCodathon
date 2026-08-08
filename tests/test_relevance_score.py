from ai.analysis.relevance_score import RelevanceScorer
from ai.models.response_parser import TopicAnalysisResponse


def main():
    analysis = TopicAnalysisResponse(
        topic="Prompt injection against AI agents",
        summary="A new technique targeting AI agents.",
        relevance_score=95,
        novelty_score=80,
        security_relevance_score=98,
    )

    scorer = RelevanceScorer()

    score = scorer.calculate(analysis)

    print("\nRELEVANCE SCORE")
    print("===============")
    print(f"Overall score: {score}")


if __name__ == "__main__":
    main()