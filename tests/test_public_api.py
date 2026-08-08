from ai.public_api import process_topic


def main():
    print("\n" + "=" * 60)
    print("STEP 4 — PUBLIC API WRAPPER TEST")
    print("=" * 60)

    assert callable(process_topic)

    print("\n✓ process_topic imported")
    print("✓ Public API is callable")

    print("\nPUBLIC API WRAPPER TEST PASSED")
    print("=" * 60)


if __name__ == "__main__":
    main()