from ai import AIEngine, process_topic


def main():
    print("\n" + "=" * 60)
    print("STEP 2 — PUBLIC AI INTERFACE TEST")
    print("=" * 60)

    assert AIEngine is not None
    assert callable(process_topic)

    print("\n✓ AIEngine exported")
    print("✓ process_topic exported")

    print("\nPUBLIC AI INTERFACE TEST PASSED")
    print("=" * 60)


if __name__ == "__main__":
    main()