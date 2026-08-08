from typing import Any


def serialize_result(result: dict[str, Any]) -> dict[str, Any]:
    """
    Convert an AIEngine result into a JSON-safe dictionary.
    """

    serialized = {}

    for key, value in result.items():

        if hasattr(value, "model_dump"):
            serialized[key] = value.model_dump()

        elif hasattr(value, "dict"):
            serialized[key] = value.dict()

        elif isinstance(value, dict):
            serialized[key] = serialize_result(value)

        elif isinstance(value, list):
            serialized[key] = [
                item.model_dump()
                if hasattr(item, "model_dump")
                else item
                for item in value
            ]

        else:
            serialized[key] = value

    return serialized