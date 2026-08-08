from typing import Any

from ai.ai_service import AIService
from ai.contracts import AIContract
from ai.result_serializer import serialize_result


class AURAAI:
    """
    Public application-facing interface for AURA's AI Brain.
    """

    def __init__(self):
        self.service = AIService()

    def process(self, topic: str) -> dict[str, Any]:
        AIContract.validate_input(topic)

        try:
            result = self.service.process_topic(topic)
            result = serialize_result(result)
            AIContract.validate_output(result)
            return result

        except (ValueError, TypeError):
            raise

        except Exception as exc:
            return {
                "status": "ERROR",
                "reason": "AI_ENGINE_FAILURE",
                "topic": topic,
                "error": str(exc),
            }

    def close(self):
        self.service.close()


def process_topic(topic: str) -> dict[str, Any]:
    ai = AURAAI()

    try:
        return ai.process(topic)
    finally:
        ai.close()