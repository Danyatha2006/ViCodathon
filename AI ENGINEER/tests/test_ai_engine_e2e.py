from ai.ai_engine import AIEngine


def main():
    print("\n" + "=" * 60)
    print("PHASE 8.2 — AI ENGINE E2E INTERFACE TEST")
    print("=" * 60)

    topic = (
        "A new runtime monitoring technique detects "
        "suspicious behavior in autonomous AI agents."
    )

    print("\nE2E topic:")
    print(topic)

    engine = AIEngine()

    assert hasattr(engine, "process_topic"), (
        "AIEngine must provide process_topic()."
    )

    result = engine.process_topic

    assert callable(result), (
        "process_topic must be callable."
    )

    print("\nAIEngine.process_topic() verified.")
    print("Complete pipeline interface is available.")

    engine.close()

    print("\n" + "=" * 60)
    print("PHASE 8.2 E2E INTERFACE TEST PASSED")
    print("=" * 60)


if __name__ == "__main__":
    main()