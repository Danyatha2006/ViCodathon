from ai.ai_engine import AIEngine
from ai.models.response_parser import (
    TopicAnalysisResponse,
    EditorialDecisionResponse,
    GeneratedPostResponse,
    RationaleResponse,
)


class FakeMemoryManager:
    """Offline memory manager."""

    def __init__(self):
        self.saved_memory = []

    def get_relevant_memory(self, topic):
        return {
            "memory": "No previous relevant coverage."
        }

    def save_post_memory(self, memory_data):
        self.saved_memory.append(memory_data)

    def close(self):
        pass


class FakeAnalyzer:
    """Offline topic analyzer."""

    def analyze(self, topic):
        return TopicAnalysisResponse(
            topic=topic,
            summary="AI security development.",
            relevance_score=95,
            novelty_score=90,
            security_relevance_score=98,
        )


class FakeScorer:
    """Offline relevance scorer."""

    def calculate(self, analysis):
        return 94.45


class FakeDuplicateChecker:
    """Configurable duplicate checker."""

    def __init__(self, is_duplicate=False):
        self.is_duplicate = is_duplicate

    def check(self, topic):
        if self.is_duplicate:
            return {
                "is_duplicate": True,
                "similar_memory": "Previously covered topic.",
                "recommendation": "REJECT_DUPLICATE",
            }

        return {
            "is_duplicate": False,
            "similar_memory": "",
            "recommendation": "PUBLISH_NEW_TOPIC",
        }


class FakeDecisionEngine:
    """Configurable editorial decision."""

    def __init__(self, decision):
        self.decision = decision

    def decide(self, analysis, overall_score):

        if self.decision == "REJECT":
            return EditorialDecisionResponse(
                decision="REJECT",
                reason="Insufficient editorial relevance.",
            )

        return EditorialDecisionResponse(
            decision="PUBLISH",
            reason="Highly relevant AI security topic.",
        )


class FakeContentGenerator:
    """Offline content generator."""

    def generate(self, *args, **kwargs):
        return GeneratedPostResponse(
            post=(
                "A new AI security technique improves "
                "monitoring of autonomous AI agents."
            )
        )


class FakeRationaleGenerator:
    """Offline rationale generator."""

    def generate(self, *args, **kwargs):
        return RationaleResponse(
            why_selected=(
                "The topic is relevant to AI security."
            ),
            why_now=(
                "Autonomous AI agents are increasingly "
                "being deployed."
            ),
            source_summary=(
                "Based on the supplied topic information."
            ),
        )


def create_engine(
    is_duplicate=False,
    decision="PUBLISH",
):
    engine = AIEngine()

    engine.memory_manager = FakeMemoryManager()
    engine.duplicate_checker = FakeDuplicateChecker(
        is_duplicate
    )

    engine.analyzer = FakeAnalyzer()
    engine.scorer = FakeScorer()

    engine.decision_engine = FakeDecisionEngine(
        decision
    )

    engine.content_generator = FakeContentGenerator()
    engine.rationale_generator = FakeRationaleGenerator()

    return engine


def test_duplicate_result():

    engine = create_engine(
        is_duplicate=True,
        decision="PUBLISH",
    )

    result = engine.process_topic(
        "Previously covered AI security topic."
    )

    assert result["status"] == "REJECTED"
    assert result["reason"] == "DUPLICATE"

    required_fields = {
        "status",
        "reason",
        "topic",
        "analysis",
        "overall_score",
        "duplicate_check",
        "memory_context",
        "decision",
    }

    assert required_fields.issubset(result.keys())

    assert "generated_post" not in result
    assert "rationale" not in result

    engine.close()


def test_editorial_rejection_result():

    engine = create_engine(
        is_duplicate=False,
        decision="REJECT",
    )

    result = engine.process_topic(
        "A trivial promotional announcement."
    )

    assert result["status"] == "REJECTED"
    assert result["reason"] == "EDITORIAL_DECISION"

    required_fields = {
        "status",
        "reason",
        "topic",
        "analysis",
        "overall_score",
        "duplicate_check",
        "memory_context",
        "decision",
    }

    assert required_fields.issubset(result.keys())

    assert "generated_post" not in result
    assert "rationale" not in result

    engine.close()


def test_publish_result():

    engine = create_engine(
        is_duplicate=False,
        decision="PUBLISH",
    )

    result = engine.process_topic(
        "A new runtime monitoring technique "
        "detects suspicious behavior in "
        "autonomous AI agents."
    )

    required_fields = {
        "status",
        "reason",
        "topic",
        "analysis",
        "overall_score",
        "duplicate_check",
        "memory_context",
        "decision",
        "generated_post",
        "rationale",
    }

    assert required_fields.issubset(result.keys())

    assert result["status"] == "PUBLISHED"
    assert result["reason"] == "APPROVED"

    assert result["generated_post"].post.strip()
    assert result["rationale"].why_selected.strip()

    engine.close()


def main():

    print("\n" + "=" * 70)
    print("PHASE 10.9 — RESULT CONTRACT INTEGRATION TEST")
    print("=" * 70)

    print("\nTesting duplicate result contract...")
    test_duplicate_result()
    print("✓ Duplicate result contract PASSED")

    print("\nTesting editorial rejection contract...")
    test_editorial_rejection_result()
    print("✓ Editorial rejection contract PASSED")

    print("\nTesting publish result contract...")
    test_publish_result()
    print("✓ Publish result contract PASSED")

    print("\n" + "=" * 70)
    print("PHASE 10.9 RESULT CONTRACT INTEGRATION TEST PASSED")
    print("=" * 70)


if __name__ == "__main__":
    main()