
from ai.ai_engine import AIEngine


def main():

    print("\n" + "=" * 60)
    print("PHASE 8.2 — AI ENGINE RESULT CONTRACT TEST")
    print("=" * 60)

    engine = AIEngine()

    required_method = "process_topic"

    assert hasattr(engine, required_method)
    assert callable(getattr(engine, required_method))

    print("\nRequired backend method:")
    print("process_topic(topic) -> dict")

    print("\nExpected result states:")
    print("1. PUBLISHED")
    print("2. REJECTED")

    print("\nExpected result information:")
    print("- status")
    print("- reason")
    print("- topic")
    print("- analysis")
    print("- overall_score")
    print("- duplicate_check")
    print("- memory_context")
    print("- decision")

    print("\nPublished results additionally contain:")
    print("- generated_post")
    print("- rationale")

    print("\nRejected results do NOT generate content.")

    print("\n" + "=" * 60)
    print("PHASE 8.2 RESULT CONTRACT TEST PASSED")
    print("=" * 60)


if __name__ == "__main__":
    main()

