from ai.ai_engine import AIEngine


def main():
    print("\n" + "=" * 60)
    print("PHASE 8.5 — AI ENGINE CONTRACT TEST")
    print("=" * 60)

    engine = AIEngine()

    print("\nChecking required public interface...")

    assert callable(engine.process_topic)
    assert callable(engine.close)

    print("✓ process_topic(topic)")
    print("✓ close()")

    print("\nChecking required pipeline components...")

    components = {
        "Topic Analyzer": "analyzer",
        "Relevance Scorer": "scorer",
        "Decision Engine": "decision_engine",
        "Content Generator": "content_generator",
        "Rationale Generator": "rationale_generator",
        "Memory Manager": "memory_manager",
        "Duplicate Checker": "duplicate_checker",
    }

    for name, attribute in components.items():
        assert getattr(engine, attribute, None) is not None
        print(f"✓ {name}")

    engine.close()

    print("\n" + "=" * 60)
    print("PHASE 8.5 AI ENGINE CONTRACT TEST PASSED")
    print("=" * 60)


if __name__ == "__main__":
    main()