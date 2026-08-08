from ai.ai_engine import AIEngine


def main():

    print("\n" + "=" * 60)
    print("PHASE 8.1 — AI ENGINE INTERFACE TEST")
    print("=" * 60)

    engine = AIEngine()

    print("\nAIEngine created successfully.")

    assert hasattr(
        engine,
        "process_topic",
    )

    assert callable(
        engine.process_topic
    )

    print(
        "process_topic() interface verified."
    )

    print("\nBackend integration interface:")

    print(
        "engine.process_topic(topic)"
    )

    print("\n" + "=" * 60)
    print("PHASE 8.1 INTERFACE TEST PASSED")
    print("=" * 60)


if __name__ == "__main__":
    main()