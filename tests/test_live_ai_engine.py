from ai.ai_engine import AIEngine


def main():
    print("\n" + "=" * 70)
    print("PHASE 9.2 — LIVE AURA AI ENGINE TEST")
    print("=" * 70)

    topic = (
        "A new runtime monitoring technique detects suspicious "
        "behavior in autonomous AI agents."
    )

    print("\nProcessing topic:")
    print(topic)

    engine = AIEngine()

    try:
        result = engine.process_topic(topic)

        print("\n=== FINAL RESULT ===")
        print("Status:", result["status"])
        print("Reason:", result["reason"])
        print("Overall score:", result["overall_score"])

        if result["status"] == "PUBLISHED":
            print("\nGenerated Post:")
            print(result["generated_post"].post)

            print("\nWhy Selected:")
            print(result["rationale"].why_selected)

            print("\nWhy Now:")
            print(result["rationale"].why_now)

            print("\nLIVE AI ENGINE TEST PASSED")

        elif result["status"] == "REJECTED":
            print("\nTopic was rejected.")
            print("Decision:", result["decision"])

    finally:
        engine.close()

    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()