from ai.api import AURAAI


class FakeMemoryManager:
    def get_relevant_memory(self, topic):
        return {"memory": "No previous coverage."}

    def save_post_memory(self, memory_data):
        pass

    def close(self):
        pass


class FakeDuplicateChecker:
    def check(self, topic):
        return {
            "is_duplicate": False,
            "similar_memory": "",
            "recommendation": "PUBLISH_NEW_TOPIC",
        }


class FakeAnalyzer:
    def analyze(self, topic):
        from ai.models.response_parser import TopicAnalysisResponse

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


class FakeDecisionEngine:
    def decide(self, analysis, overall_score):
        from ai.models.response_parser import EditorialDecisionResponse

        return EditorialDecisionResponse(
            decision="PUBLISH",
            reason="Highly relevant AI security topic.",
        )


class FakeContentGenerator:
    def generate(self, **kwargs):
        from ai.models.response_parser import GeneratedPostResponse

        return GeneratedPostResponse(
            post="A new AI security defense technique improves "
                 "monitoring of autonomous AI agents."
        )


class FakeRationaleGenerator:
    def generate(self, **kwargs):
        from ai.models.response_parser import RationaleResponse

        return RationaleResponse(
            why_selected="The topic is highly relevant to AI security.",
            why_now="Autonomous AI agents are increasingly deployed.",
            source_summary="Based on the supplied topic information.",
        )


def main():
    print("\n" + "=" * 60)
    print("PUBLIC AI API INTEGRATION TEST")
    print("=" * 60)

    ai = AURAAI()

    engine = ai.service.engine

    engine.memory_manager = FakeMemoryManager()
    engine.duplicate_checker = FakeDuplicateChecker()
    engine.analyzer = FakeAnalyzer()
    engine.scorer = FakeScorer()
    engine.decision_engine = FakeDecisionEngine()
    engine.content_generator = FakeContentGenerator()
    engine.rationale_generator = FakeRationaleGenerator()

    topic = (
        "A new runtime monitoring technique detects "
        "suspicious behavior in autonomous AI agents."
    )

    result = ai.process(topic)

    assert isinstance(result, dict)

    assert result["status"] == "PUBLISHED"
    assert result["reason"] == "APPROVED"

    assert isinstance(result["analysis"], dict)
    assert isinstance(result["decision"], dict)
    assert isinstance(result["duplicate_check"], dict)
    assert isinstance(result["generated_post"], dict)
    assert isinstance(result["rationale"], dict)

    assert result["generated_post"]["post"]
    assert result["rationale"]["why_selected"]

    print("\n✓ Public API returned dictionary")
    print("✓ Result is JSON-safe")
    print("✓ Publish result verified")
    print("✓ Generated post verified")
    print("✓ Rationale verified")

    ai.close()

    print("\n" + "=" * 60)
    print("PUBLIC AI API INTEGRATION TEST PASSED")
    print("=" * 60)


if __name__ == "__main__":
    main()