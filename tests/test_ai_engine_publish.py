from ai.ai_engine import AIEngine
from ai.models.response_parser import (
    TopicAnalysisResponse,
    EditorialDecisionResponse,
    GeneratedPostResponse,
    RationaleResponse,
)


class FakeMemoryManager:
    """Fake memory manager for the publish-path test."""

    def __init__(self):
        self.saved_memory = None

    def get_relevant_memory(self, topic):
        return {
            "memory": "No previous coverage found."
        }

    def save_post_memory(self, memory_data):
        print("\nSaving generated post to memory...")

        self.saved_memory = memory_data

    def close(self):
        pass


class FakeDuplicateChecker:
    """Simulates a genuinely new topic."""

    def check(self, topic):
        return {
            "is_duplicate": False,
            "similar_memory": "",
            "recommendation": "PUBLISH_NEW_TOPIC",
        }


class FakeAnalyzer:
    """Controlled topic analysis."""

    def analyze(self, topic):
        return TopicAnalysisResponse(
            topic=topic,
            summary=(
                "Researchers identified a new "
                "prompt injection defense technique "
                "for autonomous AI agents."
            ),
            relevance_score=95,
            novelty_score=90,
            security_relevance_score=98,
        )


class FakeScorer:

    def calculate(self, analysis):
        return 94.45


class FakeDecisionEngine:
    """Simulates a successful editorial decision."""

    def decide(self, analysis, overall_score):
        return EditorialDecisionResponse(
            decision="PUBLISH",
            reason=(
                "The topic is highly relevant to "
                "AI security, technically significant, "
                "and sufficiently novel."
            ),
        )


class FakeContentGenerator:
    """Simulates AURA's content generation."""

    def generate(
        self,
        topic,
        analysis,
        overall_score,
    ):
        print("\nGenerating AURA post...")

        return GeneratedPostResponse(
            post=(
                "A new defense technique demonstrates "
                "how runtime monitoring can help detect "
                "suspicious behavior in autonomous AI agents. "
                "The approach highlights the importance of "
                "continuous security monitoring as AI agents "
                "become more autonomous."
            )
        )


class FakeRationaleGenerator:
    """Simulates rationale generation."""

    def generate(
        self,
        topic,
        analysis,
        generated_post,
    ):
        print("\nGenerating editorial rationale...")

        return RationaleResponse(
            why_selected=(
                "The topic addresses an important "
                "AI security development."
            ),
            why_now=(
                "Autonomous AI agents are increasingly "
                "being deployed in real-world systems."
            ),
            source_summary=(
                "The rationale is based on the "
                "provided topic information."
            ),
        )


def main():

    print("\n" + "=" * 60)
    print("PHASE 7.4 — AI ENGINE FULL PUBLISH TEST")
    print("=" * 60)

    topic = (
        "A new runtime monitoring technique "
        "detects suspicious behavior in "
        "autonomous AI agents."
    )

    # Create engine.
    engine = AIEngine()

    # Create controlled test components.
    fake_memory = FakeMemoryManager()

    engine.memory_manager = fake_memory
    engine.duplicate_checker = FakeDuplicateChecker()

    engine.analyzer = FakeAnalyzer()
    engine.scorer = FakeScorer()
    engine.decision_engine = FakeDecisionEngine()

    engine.content_generator = FakeContentGenerator()
    engine.rationale_generator = FakeRationaleGenerator()

    print("\nProcessing new topic...")
    print("Topic:", topic)

    result = engine.process_topic(topic)

    print("\n=== FINAL AI ENGINE RESULT ===")

    print("Status:", result["status"])
    print("Reason:", result["reason"])

    print(
        "Decision:",
        result["decision"].decision,
    )

    print(
        "Overall score:",
        result["overall_score"],
    )

    print(
        "\nGenerated post:",
        result["generated_post"].post,
    )

    print(
        "\nWhy selected:",
        result["rationale"].why_selected,
    )

    # --------------------------------------------------
    # ASSERTIONS
    # --------------------------------------------------

    assert result["status"] == "PUBLISHED"

    assert result["reason"] == "APPROVED"

    assert (
        result["decision"].decision
        == "PUBLISH"
    )

    assert (
        result["duplicate_check"]["is_duplicate"]
        is False
    )

    assert (
        result["duplicate_check"]["recommendation"]
        == "PUBLISH_NEW_TOPIC"
    )

    assert "generated_post" in result

    assert "rationale" in result

    assert (
        result["generated_post"].post
    )

    assert (
        result["rationale"].why_selected
    )

    # Verify that memory storage happened.
    assert fake_memory.saved_memory is not None

    saved = fake_memory.saved_memory

    assert saved["agent_name"] == "AURA"

    assert (
        saved["persona"]
        == "AI Security Researcher"
    )

    assert saved["topic"] == topic

    assert saved["generated_post"]

    assert saved["rationale"]

    print("\nMemory storage verified.")

    print("\n" + "=" * 60)
    print("PHASE 7.4 FULL PUBLISH TEST PASSED")
    print("=" * 60)


if __name__ == "__main__":
    main()