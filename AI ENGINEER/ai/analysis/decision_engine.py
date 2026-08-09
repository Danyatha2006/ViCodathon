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

        AURA's primary focus is AI and AI-related technology.
        Meaningful AI-related topics should generally be published.
        """

        if not analysis:
            raise ValueError("Topic analysis is required.")

        prompt = f"""
{self.persona.get_system_prompt()}

TASK

You are AURA's editorial decision engine.

AURA is an AI-focused technology platform.

Your job is to decide whether AURA should:

PUBLISH
or
REJECT

PRIMARY PUBLISHING RULE

Any meaningful topic clearly related to Artificial Intelligence
should generally be PUBLISHED.

This includes topics involving:

- Artificial Intelligence
- AI models
- Large Language Models (LLMs)
- Generative AI
- AI agents
- AI research
- AI tools
- AI applications
- AI companies
- OpenAI
- Anthropic
- Gemini
- Google DeepMind
- Meta AI
- AI hardware
- AI infrastructure
- Machine learning systems
- AI safety
- AI security

IMPORTANT:

AI SECURITY RELEVANCE IS NOT REQUIRED for an AI-related topic
to be published.

Do NOT reject an AI-related topic simply because its
security_relevance_score is low.

A topic should generally be REJECTED only when it is:

- clearly unrelated to AI
- a duplicate or repetitive topic
- meaningless or extremely low-value
- purely promotional with no useful information
- unsupported or nonsensical

EDITORIAL GUIDELINES

Prefer meaningful technical information.

Prefer useful information over engagement bait.

Avoid unsupported claims.

Do not reject a topic merely because it is not specifically
about AI security.

AI relevance is more important than AI security relevance.

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

1. If the topic is clearly about AI or AI-related technology,
   choose PUBLISH unless it is clearly duplicate, meaningless,
   purely promotional, or unsupported.

2. Topics about AI models, LLMs, generative AI, Anthropic,
   OpenAI, Gemini, DeepMind, AI tools, AI research, AI agents,
   AI hardware, AI infrastructure, and AI applications should
   generally receive PUBLISH.

3. Do NOT require strong AI security relevance.

4. Do NOT reject an AI topic only because its overall score
   is below a preferred threshold.

5. Only choose REJECT when there is a clear editorial reason.

Return exactly one decision:

PUBLISH
or
REJECT

Also provide a concise explanation for the decision.

Return the result using the required structured format.
"""

        result = self.llm.generate_structured(
            prompt,
            EditorialDecisionResponse,
        )

        # Defensive validation
        decision = result.decision.strip().upper()

        if decision not in {"PUBLISH", "REJECT"}:
            raise RuntimeError(
                f"Invalid editorial decision returned by Gemini: "
                f"{result.decision}"
            )

        result.decision = decision

        return result