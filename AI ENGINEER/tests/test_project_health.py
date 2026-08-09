from ai.ai_engine import AIEngine

from ai.analysis.topic_analyzer import TopicAnalyzer
from ai.analysis.relevance_score import RelevanceScorer
from ai.analysis.decision_engine import DecisionEngine

from ai.generation.content_generator import ContentGenerator
from ai.generation.rationale_generator import RationaleGenerator

from ai.memory.memory_manager import MemoryManager
from ai.memory.duplicate_checker import DuplicateChecker
from ai.memory.breeth_client import BreethMemoryClient

from ai.models.llm_client import LLMClient


def main():
    print("\n" + "=" * 70)
    print("PHASE 10.1 — AURA PROJECT HEALTH CHECK")
    print("=" * 70)

    modules = [
        ("AIEngine", AIEngine),
        ("TopicAnalyzer", TopicAnalyzer),
        ("RelevanceScorer", RelevanceScorer),
        ("DecisionEngine", DecisionEngine),
        ("ContentGenerator", ContentGenerator),
        ("RationaleGenerator", RationaleGenerator),
        ("MemoryManager", MemoryManager),
        ("DuplicateChecker", DuplicateChecker),
        ("BreethMemoryClient", BreethMemoryClient),
        ("LLMClient", LLMClient),
    ]

    print("\nChecking core modules...")

    for name, module in modules:
        assert module is not None
        print(f"✓ {name}")

    print("\nAll core AURA modules imported successfully.")

    print("\n" + "=" * 70)
    print("PHASE 10.1 PROJECT HEALTH CHECK PASSED")
    print("=" * 70)


if __name__ == "__main__":
    main()