from ai.api import AURAAI


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
        from ai.models.response_parser import TopicAnalysisResponse

        return TopicAnalysisResponse(
            topic=topic,
            summary="AI security development.",
            relevance_score=95,
            novelty_score=90,
            security_relevance_score=98,
        )


class FakeScorer:
    def calculate(self, analysis):
        return 94.45


class FakeDecision:
    def decide(self, analysis, score):
        from ai.models.response_parser import EditorialDecisionResponse

        return EditorialDecisionResponse(
            decision="PUBLISH",
            reason="Highly relevant AI security topic.",
        )


class FakeContent:
    def generate(self, **kwargs):
        from ai.models.response_parser import GeneratedPostResponse

        return GeneratedPostResponse(
            post="AI security monitoring improves autonomous agents."
        )


class FakeRationale:
    def generate(self, **kwargs):
        from ai.models.response_parser import RationaleResponse

        return RationaleResponse(
            why_selected="Relevant AI security topic.",
            why_now="Autonomous agents are increasingly deployed.",
            source_summary="Based on supplied topic information.",
        )


def main():
    print("\n" + "=" * 60)
    print("FINAL AI PUBLIC CONTRACT TEST")
    print("=" * 60)

    ai = AURAAI()
    engine = ai.service.engine

    engine.memory_manager = FakeMemory()
    engine.duplicate_checker = FakeDuplicate()
    engine.analyzer = FakeAnalyzer()
    engine.scorer = FakeScorer()
    engine.decision_engine = FakeDecision()
    engine.content_generator = FakeContent()
    engine.rationale_generator = FakeRationale()

    result = ai.process(
        "A new runtime monitoring technique detects "
        "suspicious behavior in autonomous AI agents."
    )

    assert isinstance(result, dict)

    required = {
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

    assert required.issubset(result.keys())

    assert result["status"] == "PUBLISHED"
    assert result["reason"] == "APPROVED"

    assert isinstance(result["analysis"], dict)
    assert isinstance(result["decision"], dict)
    assert isinstance(result["generated_post"], dict)
    assert isinstance(result["rationale"], dict)

    print("\n✓ Input contract")
    print("✓ Output contract")
    print("✓ JSON-safe result")
    print("✓ Published result")
    print("✓ Generated post")
    print("✓ Rationale")

    ai.close()

    print("\n" + "=" * 60)
    print("FINAL AI PUBLIC CONTRACT TEST PASSED")
    print("=" * 60)


if __name__ == "__main__":
    main()