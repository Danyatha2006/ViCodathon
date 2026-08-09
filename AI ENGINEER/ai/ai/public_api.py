from typing import Any

from ai.ai_engine import AIEngine


def process_topic(topic: str) -> dict[str, Any]:
    """
    Public entry point for the AURA AI Brain.
    """

    engine = AIEngine()

    try:
        return engine.process_topic(topic)
    finally:
        engine.close()