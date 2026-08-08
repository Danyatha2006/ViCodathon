from typing import Any

from ai.memory.memory_manager import MemoryManager


class DuplicateChecker:
    """
    Detects whether a new topic is already covered by AURA.

    Decisions:
    - REJECT_DUPLICATE: same topic/event already covered
    - NEW_PERSPECTIVE: related topic but different development
    - PUBLISH_NEW_TOPIC: no meaningful previous coverage
    """

    def __init__(
        self,
        memory_manager: MemoryManager | None = None,
    ):
        self.memory = memory_manager or MemoryManager()

    def check(self, topic: str) -> dict[str, Any]:
        if not topic or not topic.strip():
            raise ValueError("Topic cannot be empty.")

        results = self.memory.check_previous_discussion(
            topic,
            limit=5,
        )

        if not results:
            return self._new_topic_result()

        edges = getattr(results, "edges", [])

        if not edges:
            return self._new_topic_result()

        best_match = ""
        best_score = 0.0

        for edge in edges:
            fact = getattr(edge, "fact", "")

            if not fact:
                continue

            score = self._similarity_score(
                topic,
                fact,
            )

            if score > best_score:
                best_score = score
                best_match = fact

        # Same distinctive topic.
        if best_score >= 0.80:
            return {
                "is_duplicate": True,
                "similar_memory": best_match,
                "recommendation": "REJECT_DUPLICATE",
            }

        # Related topic, but not the same topic.
        if best_score >= 0.30:
            return {
                "is_duplicate": False,
                "similar_memory": best_match,
                "recommendation": "NEW_PERSPECTIVE",
            }

        return {
            "is_duplicate": False,
            "similar_memory": best_match,
            "recommendation": "PUBLISH_NEW_TOPIC",
        }

    @staticmethod
    def _similarity_score(
        topic: str,
        memory_text: str,
    ) -> float:
        """
        Calculate similarity using both:
        1. distinctive phrase overlap
        2. meaningful word overlap

        Phrase overlap is important because a memory may contain
        the same topic inside a longer sentence.
        """

        topic_words = DuplicateChecker._important_words(topic)
        memory_words = DuplicateChecker._important_words(
            memory_text
        )

        if not topic_words or not memory_words:
            return 0.0

        intersection = topic_words.intersection(
            memory_words
        )

        # How much of the NEW topic's distinctive vocabulary
        # is present in the previous memory?
        topic_coverage = (
            len(intersection) / len(topic_words)
        )

        # How much of the memory's vocabulary is shared?
        memory_coverage = (
            len(intersection) / len(memory_words)
        )

        # Strong coverage of the new topic is more important
        # than the extra descriptive words in the memory.
        score = (
            topic_coverage * 0.75
            + memory_coverage * 0.25
        )

        return score

    @staticmethod
    def _important_words(text: str) -> set[str]:
        """
        Extract distinctive topic words.

        Generic AI/security vocabulary is removed because
        those words alone do not prove duplication.
        """

        stop_words = {
            "the",
            "a",
            "an",
            "in",
            "on",
            "of",
            "to",
            "and",
            "for",
            "is",
            "are",
            "with",
            "new",
            "how",
            "this",
            "that",
            "used",
            "into",
            "from",
            "can",
            "has",
            "have",
            "been",
            "about",
            "through",
            "allows",
            "allow",
            "using",
            "uses",

            # Generic AI/security terms
            "ai",
            "artificial",
            "intelligence",
            "agent",
            "agents",
            "autonomous",
            "security",
            "secure",
            "technique",
            "techniques",
            "attack",
            "attacks",
            "researcher",
            "researchers",
            "system",
            "systems",
            "safety",
            "controls",
            "control",
            "identifies",
            "identify",
            "identified",
        }

        words = (
            word.strip(".,!?():;\"'").lower()
            for word in text.split()
        )

        return {
            word
            for word in words
            if len(word) >= 4
            and word not in stop_words
        }

    @staticmethod
    def _new_topic_result() -> dict[str, Any]:
        return {
            "is_duplicate": False,
            "similar_memory": "",
            "recommendation": "PUBLISH_NEW_TOPIC",
        }

    def close(self) -> None:
        self.memory.close()