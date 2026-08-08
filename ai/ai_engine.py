from typing import Any

from ai.analysis.topic_analyzer import TopicAnalyzer
from ai.analysis.relevance_score import RelevanceScorer
from ai.analysis.decision_engine import DecisionEngine
from ai.generation.content_generator import ContentGenerator
from ai.generation.rationale_generator import RationaleGenerator
from ai.memory.memory_manager import MemoryManager
from ai.memory.duplicate_checker import DuplicateChecker


class AIEngine:
    """
    Main orchestration layer for AURA's AI intelligence.

    Flow:

    Topic
        ↓
    Memory Search
        ↓
    Topic Analysis
        ↓
    Relevance Scoring
        ↓
    Duplicate Check
        ↓
    Editorial Decision
        ↓
    Content Generation
        ↓
    Rationale Generation
        ↓
    Memory Storage
    """

    def __init__(self):
        self.analyzer = TopicAnalyzer()
        self.scorer = RelevanceScorer()
        self.decision_engine = DecisionEngine()

        self.content_generator = ContentGenerator()
        self.rationale_generator = RationaleGenerator()

        self.memory_manager = MemoryManager()
        self.duplicate_checker = DuplicateChecker(
            self.memory_manager
        )

    def process_topic(self, topic: str) -> dict[str, Any]:
        """
        Process one discovered topic through the complete
        AURA intelligence pipeline.
        """

        if not topic or not topic.strip():
            raise ValueError("Topic cannot be empty.")

        # --------------------------------------------------
        # 1. MEMORY SEARCH
        # --------------------------------------------------

        memory_context = self.memory_manager.get_relevant_memory(
            topic
        )

        # --------------------------------------------------
        # 2. TOPIC ANALYSIS
        # --------------------------------------------------

        analysis = self.analyzer.analyze(topic)

        # --------------------------------------------------
        # 3. RELEVANCE SCORING
        # --------------------------------------------------

        overall_score = self.scorer.calculate(
            analysis
        )

        # --------------------------------------------------
        # 4. DUPLICATE CHECK
        # --------------------------------------------------

        duplicate_result = self.duplicate_checker.check(
            topic
        )

        # --------------------------------------------------
        # 5. DUPLICATE REJECTION
        # --------------------------------------------------

        if duplicate_result["is_duplicate"]:

            return {
                "status": "REJECTED",
                "reason": "DUPLICATE",
                "topic": topic,
                "analysis": analysis,
                "overall_score": overall_score,
                "duplicate_check": duplicate_result,
                "memory_context": memory_context,
                "decision": {
                    "decision": "REJECT",
                    "reason": (
                        "The topic has already been "
                        "covered by AURA."
                    ),
                },
            }

        # --------------------------------------------------
        # 6. EDITORIAL DECISION
        # --------------------------------------------------

        decision = self.decision_engine.decide(
            analysis,
            overall_score,
        )

        # --------------------------------------------------
        # 7. REJECT WEAK TOPICS
        # --------------------------------------------------

        if decision.decision.upper() != "PUBLISH":

            return {
                "status": "REJECTED",
                "reason": "EDITORIAL_DECISION",
                "topic": topic,
                "analysis": analysis,
                "overall_score": overall_score,
                "duplicate_check": duplicate_result,
                "memory_context": memory_context,
                "decision": decision,
            }

        # --------------------------------------------------
        # 8. GENERATE CONTENT
        # --------------------------------------------------

        generated_post = self.content_generator.generate(
            topic=topic,
            analysis=analysis,
            overall_score=overall_score,
        )

        # --------------------------------------------------
        # 9. GENERATE RATIONALE
        # --------------------------------------------------

        rationale = self.rationale_generator.generate(
            topic=topic,
            analysis=analysis,
            generated_post=generated_post,
        )

        # --------------------------------------------------
        # 10. SAVE MEMORY
        # --------------------------------------------------

        memory_data = {
            "agent_name": "AURA",
            "persona": "AI Security Researcher",
            "topic": topic,
            "summary": analysis.summary,
            "generated_post": generated_post.post,
            "rationale": rationale.why_selected,
            "sources": [],
            "timestamp": "",
        }

        self.memory_manager.save_post_memory(
            memory_data
        )

        # --------------------------------------------------
        # 11. RETURN COMPLETE RESULT
        # --------------------------------------------------

        return {
            "status": "PUBLISHED",
            "reason": "APPROVED",
            "topic": topic,
            "analysis": analysis,
            "overall_score": overall_score,
            "duplicate_check": duplicate_result,
            "memory_context": memory_context,
            "decision": decision,
            "generated_post": generated_post,
            "rationale": rationale,
        }

    def close(self):
        """Close the underlying memory connection."""

        self.memory_manager.close()