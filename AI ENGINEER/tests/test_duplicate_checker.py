from ai.memory.duplicate_checker import DuplicateChecker


def main():

    print("\n=== DUPLICATE CHECKER TEST ===")

    checker = DuplicateChecker()

    topic = "Indirect Prompt Injection in Autonomous AI Agents"

    print("\nChecking topic:")
    print(topic)

    result = checker.check(topic)

    print("\n=== DUPLICATE RESULT ===")
    print("Is duplicate:", result["is_duplicate"])
    print("Similar memory:", result["similar_memory"])
    print("Recommendation:", result["recommendation"])

    if result["is_duplicate"] is not True:
        raise AssertionError(
            "The previously stored topic should be detected as a duplicate."
        )

    if result["recommendation"] != "REJECT_DUPLICATE":
        raise AssertionError(
            "Duplicate topic should receive REJECT_DUPLICATE recommendation."
        )

    print("\nDUPLICATE DETECTION TEST PASSED")

    checker.close()


if __name__ == "__main__":
    main()