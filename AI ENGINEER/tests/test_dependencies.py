def main():
    print("\n" + "=" * 70)
    print("PHASE 10.3 — DEPENDENCY HEALTH TEST")
    print("=" * 70)

    required_packages = {
        "google.genai": "Gemini SDK",
        "breeth": "Breeth SDK",
        "dotenv": "python-dotenv",
        "pydantic": "Pydantic",
    }

    print("\nChecking required packages...")

    for module, name in required_packages.items():
        try:
            __import__(module)
            print(f"✓ {name}")
        except ImportError as exc:
            raise AssertionError(
                f"{name} is missing: {exc}"
            )

    print("\nAll required packages are available.")

    print("\n" + "=" * 70)
    print("PHASE 10.3 DEPENDENCY HEALTH TEST PASSED")
    print("=" * 70)


if __name__ == "__main__":
    main()