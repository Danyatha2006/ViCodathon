from integration.ai_brain_adapter import AIBrainAdapter
from ai.models.response_parser import (
    TopicAnalysisResponse,
    EditorialDecisionResponse,
    GeneratedPostResponse,
    RationaleResponse,
)


class FakeMemory:
    def get_relevant_memory(self, topic):
        return {"memory": "No previous coverage."}

    def save_post_memory(self, data):
        pass

    def close(self):
        pass


class FakeDuplicate:
    def check(self, topic):
        return {
            "is_duplicate": False,
            "similar_memory": "",
            "recommendation": "PUBLISH_NEW_TOPIC",
        }


class FakeAnalyzer:
    def analyze(self, topic):
        return TopicAnalysisResponse(
            topic=topic,
            summary="Important AI security development.",
            relevance_score=95,
            novelty_score=90,
            security_relevance_score=98,
        )


class FakeScorer:
    def calculate(self, analysis):
        return 94.45


class FakeDecision:
    def decide(self, analysis, score):
        return EditorialDecisionResponse(
            decision="PUBLISH",
            reason="Highly relevant AI security topic.",
        )


class FakeContent:
    def generate(self, **kwargs):
        return GeneratedPostResponse(
            post="A new AI security defense improves monitoring."
        )


class FakeRationale:
    def generate(self, **kwargs):
        return RationaleResponse(
            why_selected="Relevant AI security development.",
            why_now="Autonomous AI systems are increasingly deployed.",
            source_summary="Based on supplied topic information.",
        )


def main():

    print("=" * 70)
    print("FINAL OFFLINE TEAM INTEGRATION TEST")
    print("=" * 70)

    brain = AIBrainAdapter()

    engine = brain.ai.service.engine

    engine.memory_manager = FakeMemory()
    engine.duplicate_checker = FakeDuplicate()
    engine.analyzer = FakeAnalyzer()
    engine.scorer = FakeScorer()
    engine.decision_engine = FakeDecision()
    engine.content_generator = FakeContent()
    engine.rationale_generator = FakeRationale()

    topic = (
        "A new runtime monitoring technique detects "
        "suspicious behavior in autonomous AI agents."
    )

    result = brain.process_topic(topic)

    assert result["status"] == "PUBLISHED"
    assert result["reason"] == "APPROVED"
    assert result["topic"] == topic
    assert result["overall_score"] == 94.45
    assert result["decision"]["decision"] == "PUBLISH"
    assert result["generated_post"]["post"]
    assert result["rationale"]["why_selected"]

    print("✓ Adapter works")
    print("✓ Topic processed")
    print("✓ Decision returned")
    print("✓ Generated post returned")
    print("✓ Rationale returned")
    print("✓ JSON-safe result returned")
    print("✓ No Gemini API call required")

    brain.close()

    print("=" * 70)
    print("FINAL OFFLINE TEAM INTEGRATION TEST PASSED")
    print("=" * 70)


if __name__ == "__main__":
    main()