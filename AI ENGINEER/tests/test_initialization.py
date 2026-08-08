from ai.ai_engine import AIEngine


def main():
    print("\n" + "=" * 70)
    print("PHASE 10.5 — AI ENGINE INITIALIZATION TEST")
    print("=" * 70)

    print("\nInitializing AIEngine...")

    engine = AIEngine()

    print("✓ AIEngine initialized successfully")

    required_components = [
        "analyzer",
        "scorer",
        "decision_engine",
        "content_generator",
        "rationale_generator",
        "memory_manager",
        "duplicate_checker",
    ]

    print("\nChecking initialized components...")

    for component in required_components:
        if not hasattr(engine, component):
            raise AssertionError(
                f"Missing AIEngine component: {component}"
            )

        print(f"✓ {component}")

    engine.close()

    print("\n✓ AIEngine closed successfully")

    print("\n" + "=" * 70)
    print("PHASE 10.5 INITIALIZATION TEST PASSED")
    print("=" * 70)


if __name__ == "__main__":
    main()