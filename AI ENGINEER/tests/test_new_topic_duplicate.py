from ai.memory.duplicate_checker import DuplicateChecker


def main():

    print("\n=== NEW TOPIC DUPLICATE TEST ===")

    checker = DuplicateChecker()

    topic = (
        "A new defense technique uses runtime monitoring "
        "to detect suspicious behavior in autonomous AI agents."
    )

    print("\nChecking topic:")
    print(topic)

    result = checker.check(topic)

    print("\n=== RESULT ===")
    print("Is duplicate:", result["is_duplicate"])
    print("Similar memory:", result["similar_memory"])
    print("Recommendation:", result["recommendation"])

    if result["is_duplicate"]:
        raise AssertionError(
            "A genuinely different topic should not be "
            "automatically classified as an exact duplicate."
        )

    if result["recommendation"] != "PUBLISH_NEW_TOPIC":
        raise AssertionError(
            "New topic should receive PUBLISH_NEW_TOPIC."
        )

    print("\nNEW TOPIC TEST PASSED")

    checker.close()


if __name__ == "__main__":
    main()