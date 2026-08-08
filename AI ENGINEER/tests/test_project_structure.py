from pathlib import Path


def main():
    print("\n" + "=" * 70)
    print("PHASE 10.4 — PROJECT STRUCTURE TEST")
    print("=" * 70)

    root = Path(__file__).resolve().parent.parent

    required_paths = [
        "ai/ai_engine.py",
        "ai/analysis/topic_analyzer.py",
        "ai/analysis/relevance_score.py",
        "ai/analysis/decision_engine.py",
        "ai/generation/content_generator.py",
        "ai/generation/rationale_generator.py",
        "ai/memory/memory_manager.py",
        "ai/memory/duplicate_checker.py",
        "ai/memory/breeth_client.py",
        "ai/models/llm_client.py",
        "tests",
        ".env",
    ]

    print("\nChecking required project files...")

    for relative_path in required_paths:
        path = root / relative_path

        if not path.exists():
            raise AssertionError(
                f"Missing required path: {relative_path}"
            )

        print(f"✓ {relative_path}")

    print("\nProject structure is valid.")

    print("\n" + "=" * 70)
    print("PHASE 10.4 PROJECT STRUCTURE TEST PASSED")
    print("=" * 70)


if __name__ == "__main__":
    main()