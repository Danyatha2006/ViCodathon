from ai.ai_engine import AIEngine


def main():
    print("\n" + "=" * 60)
    print("PHASE 8.4 — AI ENGINE STRUCTURE TEST")
    print("=" * 60)

    engine = AIEngine()

    required_components = [
        "analyzer",
        "scorer",
        "decision_engine",
        "content_generator",
        "rationale_generator",
        "memory_manager",
        "duplicate_checker",
    ]

    print("\nChecking AI Engine components...")

    for component in required_components:
        assert hasattr(engine, component), (
            f"Missing AIEngine component: {component}"
        )

        print(f"✓ {component}")

    assert callable(engine.process_topic)
    assert callable(engine.close)

    print("\n✓ process_topic() available")
    print("✓ close() available")

    engine.close()

    print("\n" + "=" * 60)
    print("PHASE 8.4 AI ENGINE STRUCTURE TEST PASSED")
    print("=" * 60)


if __name__ == "__main__":
    main()