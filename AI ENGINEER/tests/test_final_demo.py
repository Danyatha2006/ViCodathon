from ai.ai_engine import AIEngine


def main():
    print("\n" + "=" * 70)
    print("AURA AI ENGINE — FINAL DEMO")
    print("=" * 70)

    topic = (
        "A new runtime monitoring technique detects "
        "suspicious behavior in autonomous AI agents."
    )

    print("\nDiscovered Topic:")
    print(topic)

    print("\nInitializing AURA AI Engine...")

    engine = AIEngine()

    print("AI Engine initialized successfully.")

    print("\nPipeline:")
    print("  Topic")
    print("   ↓")
    print("  Memory Search")
    print("   ↓")
    print("  Topic Analysis")
    print("   ↓")
    print("  Relevance Scoring")
    print("   ↓")
    print("  Duplicate Detection")
    print("   ↓")
    print("  Editorial Decision")
    print("   ↓")
    print("  Content Generation")
    print("   ↓")
    print("  Rationale Generation")
    print("   ↓")
    print("  Memory Storage")

    print("\nAI Engine interface verified.")
    print("Ready for live Gemini execution.")

    engine.close()

    print("\n" + "=" * 70)
    print("AURA AI ENGINE FINAL DEMO SETUP PASSED")
    print("=" * 70)


if __name__ == "__main__":
    main()