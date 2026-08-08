from ai.models.llm_client import LLMClient
from ai.models.response_parser import (
    TopicAnalysisResponse,
    EditorialDecisionResponse,
)
from ai.persona.persona import AURAPersona


class DecisionEngine:
    """Makes AURA's final editorial publishing decision."""

    def __init__(self):
        self.llm = LLMClient()
        self.persona = AURAPersona()

    def decide(
        self,
        analysis: TopicAnalysisResponse,
        overall_score: float,
    ) -> EditorialDecisionResponse:
        """
        Decide whether AURA should publish or reject a topic.

        The decision is based on:
        - Overall topic score
        - Relevance
        - Novelty
        - AI security relevance
        - AURA's editorial principles
        """

        if not analysis:
            raise ValueError("Topic analysis is required.")

        prompt = f"""
{self.persona.get_system_prompt()}

TASK

You are AURA's editorial decision engine.

You have received an analyzed technology topic.

Your job is to decide whether AURA should:

PUBLISH
or
REJECT

IMPORTANT:

The decision must NOT always be PUBLISH.

AURA should reject topics that are:
- trivial
- weakly related to AI security
- low-value
- repetitive
- overly generic
- primarily promotional
- unsupported by meaningful technical information
- not useful to AURA's audience

AURA should publish topics that are:
- technically significant
- relevant to AI security
- sufficiently novel
- useful to the audience
- supported by meaningful information
- aligned with AURA's editorial mission

EDITORIAL GUIDELINES

Prefer technical significance over popularity.

Prefer useful insight over engagement bait.

Avoid unnecessary hype.

Do not publish simply because a topic is trending.

Do not make unsupported claims.

Distinguish facts from interpretation.

INPUT TOPIC

Topic:
{analysis.topic}

Summary:
{analysis.summary}

Relevance score:
{analysis.relevance_score}/100

Novelty score:
{analysis.novelty_score}/100

Security relevance score:
{analysis.security_relevance_score}/100

Overall weighted score:
{overall_score}/100

DECISION RULES

Use the scores as important evidence, but do not blindly follow the
overall score.

A topic with weak AI security relevance should generally be rejected.

A topic with very low relevance or very low novelty should generally
be rejected unless there is a strong editorial reason to publish it.

A strong topic with meaningful AI security implications should generally
be published.

Return exactly one decision:

PUBLISH
or
REJECT

Also provide a concise explanation of why AURA made that decision.

Return the result using the required structured format.
"""

        result = self.llm.generate_structured(
            prompt,
            EditorialDecisionResponse,
        )

        # Defensive validation so downstream modules never receive
        # an unexpected decision value.
        decision = result.decision.strip().upper()

        if decision not in {"PUBLISH", "REJECT"}:
            raise RuntimeError(
                f"Invalid editorial decision returned by Gemini: "
                f"{result.decision}"
            )

        result.decision = decision

        return result