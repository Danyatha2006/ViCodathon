from typing import Any

from ai import AURAAI


class AIBrainAdapter:
    """Team-facing adapter for the AURA AI Brain."""

    def __init__(self):
        self.ai = AURAAI()

    def process_topic(self, topic: str) -> dict[str, Any]:
        if not topic or not topic.strip():
            raise ValueError("Topic cannot be empty.")

        return self.ai.process(topic)

    def close(self):
        self.ai.close()