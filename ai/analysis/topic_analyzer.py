from ai.models.llm_client import LLMClient
from ai.models.response_parser import TopicAnalysisResponse
from ai.persona.persona import AURAPersona


class TopicAnalyzer:
    """Analyzes discovered topics using AURA's editorial criteria."""

    def __init__(self):
        self.llm = LLMClient()
        self.persona = AURAPersona()

    def analyze(self, topic: str) -> TopicAnalysisResponse:
        """Analyze a topic and return structured analysis."""

        if not topic or not topic.strip():
            raise ValueError("Topic cannot be empty.")

        prompt = f"""
{self.persona.get_system_prompt()}

TASK

Analyze the following newly discovered technology topic.

TOPIC:
{topic}

Evaluate it specifically for AURA.

Consider:

1. Relevance to AI and technology.
2. Relevance to AI security.
3. Technical significance.
4. Novelty.
5. Potential value to AURA's audience.

Do not decide whether to publish yet.
Only perform the topic analysis.

Return the result using the required structured format.
"""

        return self.llm.generate_structured(
            prompt,
            TopicAnalysisResponse,
        )
    