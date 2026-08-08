from ai.ai_engine import AIEngine


def main():
    print("\n" + "=" * 60)
    print("PHASE 8.3 — AI ENGINE INVALID INPUT TEST")
    print("=" * 60)

    engine = AIEngine()

    invalid_topics = [
        "",
        "   ",
    ]

    for topic in invalid_topics:
        print("\nTesting invalid topic:", repr(topic))

        try:
            engine.process_topic(topic)

            raise AssertionError(
                "AIEngine should reject an empty topic."
            )

        except ValueError as exc:
            print("Expected error caught:")
            print(exc)

    engine.close()

    print("\n" + "=" * 60)
    print("PHASE 8.3 INVALID INPUT TEST PASSED")
    print("=" * 60)


if __name__ == "__main__":
    main()