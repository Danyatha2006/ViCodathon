from datetime import datetime, timezone
from typing import Any, Optional

from ai.memory.breeth_client import BreethMemoryClient


class MemoryManager:
    """Manages AURA's long-term memory through Breeth."""

    def __init__(
        self,
        breeth_client: Optional[BreethMemoryClient] = None,
    ):
        self.breeth = breeth_client or BreethMemoryClient()

    def save_post_memory(
        self,
        post: dict[str, Any],
    ) -> Any:
        """
        Save a published post and its editorial context to Breeth.
        """

        if not post:
            raise ValueError("Post memory cannot be empty.")

        topic = post.get("topic", "")

        if not topic or not topic.strip():
            raise ValueError(
                "Post memory must contain a topic."
            )

        memory_data = {
            "agent_name": "AURA",
            "persona": "AI Security Researcher",
            "topic": topic,
            "summary": post.get("summary", ""),
            "generated_post": post.get("generated_post", ""),
            "rationale": post.get("rationale", ""),
            "sources": post.get("sources", []),
            "timestamp": post.get(
                "timestamp",
                datetime.now(timezone.utc).isoformat(),
            ),
        }

        return self.breeth.store_memory(memory_data)

    def get_relevant_memory(
        self,
        topic: str,
        limit: int = 5,
    ) -> Any:
        """
        Retrieve memories relevant to a new topic.
        """

        if not topic or not topic.strip():
            raise ValueError("Topic cannot be empty.")

        return self.breeth.retrieve_memory(
            topic,
            limit=limit,
        )

    def check_previous_discussion(
        self,
        topic: str,
        limit: int = 5,
    ) -> Any:
        """
        Search for previous discussions related to a topic.
        """

        if not topic or not topic.strip():
            raise ValueError("Topic cannot be empty.")

        return self.breeth.search_similar_topics(
            topic,
            limit=limit,
        )

    def close(self) -> None:
        """Close the underlying Breeth client."""

        self.breeth.close()