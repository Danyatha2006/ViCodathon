from dataclasses import asdict, is_dataclass
from typing import Any

from ai.ai_engine import AIEngine
from ai.public_api import process_topic


def _serialize(value: Any) -> Any:
    """Convert AI response objects into JSON-safe Python data."""

    if is_dataclass(value):
        return {
            key: _serialize(item)
            for key, item in asdict(value).items()
        }

    if isinstance(value, dict):
        return {
            key: _serialize(item)
            for key, item in value.items()
        }

    if isinstance(value, list):
        return [_serialize(item) for item in value]

    if hasattr(value, "model_dump"):
        return _serialize(value.model_dump())

    return value


class _AIService:
    """Internal service container used by the public AURA interface."""

    def __init__(self):
        self.engine = AIEngine()

    def close(self):
        self.engine.close()


class AURAAI:
    """Official team-facing AURA AI Brain interface."""

    def __init__(self):
        self.service = _AIService()

    def process(self, topic: str) -> dict[str, Any]:
        result = self.service.engine.process_topic(topic)
        return _serialize(result)

    def close(self):
        self.service.close()


__all__ = [
    "AIEngine",
    "AURAAI",
    "process_topic",
]