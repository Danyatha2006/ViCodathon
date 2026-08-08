import os
from typing import Any, Optional

from dotenv import load_dotenv
from breeth import BreethClient, BreethError


load_dotenv()


class BreethMemoryClient:
    """Adapter around the official Breeth Python SDK."""

    DEFAULT_GROUP_ID = "aura"

    def __init__(self, group_id: Optional[str] = None):
        self.api_key = os.getenv("BREETH_API_KEY")

        if not self.api_key:
            raise RuntimeError(
                "BREETH_API_KEY is not configured. "
                "Add it to the .env file."
            )

        self.group_id = group_id or self.DEFAULT_GROUP_ID
        self.client = BreethClient(api_key=self.api_key)

    def connect_breeth(self) -> bool:
        """
        Verify that the Breeth client can communicate with Breeth.

        A lightweight retrieval request is used because the official
        SDK exposes retrieve() for memory retrieval.
        """

        try:
            self.client.retrieve(
                "AURA AI Security Researcher",
                group_id=self.group_id,
                limit=1,
            )
            return True

        except BreethError as exc:
            raise RuntimeError(
                f"Breeth connection failed: {exc}"
            ) from exc

    def store_memory(self, memory_data: dict[str, Any]) -> Any:
        """
        Store a memory in Breeth.

        The memory dictionary is converted into a structured prose
        episode because Breeth's write() API accepts prose memory.
        """

        if not memory_data:
            raise ValueError("Memory data cannot be empty.")

        topic = memory_data.get("topic", "")
        summary = memory_data.get("summary", "")
        generated_post = memory_data.get("generated_post", "")
        rationale = memory_data.get("rationale", "")
        sources = memory_data.get("sources", [])
        timestamp = memory_data.get("timestamp", "")

        content = f"""
Agent: {memory_data.get("agent_name", "AURA")}
Persona: {memory_data.get("persona", "AI Security Researcher")}
Topic: {topic}
Summary: {summary}
Generated Post: {generated_post}
Editorial Rationale: {rationale}
Sources: {sources}
Timestamp: {timestamp}
""".strip()

        try:
            return self.client.write(
                content,
                group_id=self.group_id,
            )

        except BreethError as exc:
            raise RuntimeError(
                f"Breeth memory write failed: {exc}"
            ) from exc

    def retrieve_memory(
        self,
        query: str,
        limit: int = 5,
    ) -> Any:
        """Retrieve relevant memories from Breeth."""

        if not query or not query.strip():
            raise ValueError("Memory query cannot be empty.")

        if limit < 1 or limit > 100:
            raise ValueError("Limit must be between 1 and 100.")

        try:
            return self.client.retrieve(
                query.strip(),
                group_id=self.group_id,
                limit=limit,
            )

        except BreethError as exc:
            raise RuntimeError(
                f"Breeth memory retrieval failed: {exc}"
            ) from exc

    def search_similar_topics(
        self,
        topic: str,
        limit: int = 5,
    ) -> Any:
        """Search Breeth for memories related to a topic."""

        if not topic or not topic.strip():
            raise ValueError("Topic cannot be empty.")

        return self.retrieve_memory(
            query=topic,
            limit=limit,
        )

    def close(self) -> None:
        """Close the Breeth client."""

        self.client.close()