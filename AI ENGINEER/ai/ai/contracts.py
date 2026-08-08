from typing import Any


class AIContract:
    """
    Public contract between AURA AI Brain and the rest
    of the application.
    """

    @staticmethod
    def validate_input(topic: Any) -> None:
        if not isinstance(topic, str):
            raise TypeError("topic must be a string.")

        if not topic.strip():
            raise ValueError("topic cannot be empty.")

    @staticmethod
    def validate_output(result: Any) -> None:
        if not isinstance(result, dict):
            raise TypeError("AI result must be a dictionary.")

        required = {
            "status",
            "reason",
            "topic",
            "analysis",
            "overall_score",
            "duplicate_check",
            "memory_context",
            "decision",
        }

        missing = required - result.keys()

        if missing:
            raise ValueError(
                f"AI result missing fields: {sorted(missing)}"
            )

        if result["status"] not in {"PUBLISHED", "REJECTED"}:
            raise ValueError("Invalid AI result status.")

        if result["status"] == "PUBLISHED":
            if "generated_post" not in result:
                raise ValueError(
                    "Published result must contain generated_post."
                )

            if "rationale" not in result:
                raise ValueError(
                    "Published result must contain rationale."
                )