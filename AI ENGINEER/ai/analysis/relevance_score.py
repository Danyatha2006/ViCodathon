from ai.models.response_parser import TopicAnalysisResponse


class RelevanceScorer:
    """Calculates AURA's overall topic score."""

    RELEVANCE_WEIGHT = 0.35
    NOVELTY_WEIGHT = 0.25
    SECURITY_WEIGHT = 0.40

    def calculate(
        self,
        analysis: TopicAnalysisResponse,
    ) -> float:
        """Calculate the weighted topic score."""

        score = (
            analysis.relevance_score
            * self.RELEVANCE_WEIGHT
            + analysis.novelty_score
            * self.NOVELTY_WEIGHT
            + analysis.security_relevance_score
            * self.SECURITY_WEIGHT
        )

        return round(score, 2)