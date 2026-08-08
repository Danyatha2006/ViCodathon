from ai.models.llm_client import LLMClient
from ai.models.response_parser import (
    TopicAnalysisResponse,
    GeneratedPostResponse,
)
from ai.persona.persona import AURAPersona


class ContentGenerator:
    """Generates AURA's final editorial post."""

    def __init__(self):
        self.llm = LLMClient()
        self.persona = AURAPersona()

    def generate(
        self,
        analysis: TopicAnalysisResponse,
    ) -> GeneratedPostResponse:
        """
        Generate a final post from an approved topic analysis.
        """

        if not analysis:
            raise ValueError("Topic analysis is required.")

        prompt = f"""
{self.persona.get_system_prompt()}

TASK

Write a final editorial post for AURA based on the approved topic below.

AURA is an AI Security Researcher.

The post must:

- Clearly explain the important development.
- Focus on the technical significance.
- Explain why the development matters.
- Be concise and informative.
- Maintain AURA's analytical and evidence-driven voice.
- Avoid unnecessary hype.
- Avoid clickbait.
- Avoid exaggerated claims.
- Do not invent facts.
- Do not add information that is not supported by the provided topic.
- Distinguish the known information from interpretation.
- Do not use generic promotional language.

TOPIC

{analysis.topic}

SUMMARY

{analysis.summary}

RELEVANCE SCORE

{analysis.relevance_score}/100

NOVELTY SCORE

{analysis.novelty_score}/100

SECURITY RELEVANCE SCORE

{analysis.security_relevance_score}/100

Write the final post now.

Return the result using the required structured format.
"""

        result = self.llm.generate_structured(
            prompt,
            GeneratedPostResponse,
        )

        if not result.post or not result.post.strip():
            raise RuntimeError(
                "Content generator returned an empty post."
            )

        result.post = result.post.strip()

        return result