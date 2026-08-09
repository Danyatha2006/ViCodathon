from typing import Any

from ai.ai_engine import AIEngine


class AIService:
    """
    Team-facing service wrapper for the AURA AI Engine.
    """

    def __init__(self):
        self.engine = AIEngine()

    def process_topic(self, topic: str) -> dict[str, Any]:
        """
        Process a discovered topic through the AURA AI pipeline.
        """
        return self.engine.process_topic(topic)

    def close(self):
        """
        Close AI Engine resources.
        """
        self.engine.close()