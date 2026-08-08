from ai.memory.memory_manager import MemoryManager


def main():

    print("\n=== MEMORY MANAGER TEST ===")

    manager = MemoryManager()

    topic = "Indirect Prompt Injection in Autonomous AI Agents"

    print("\nRetrieving relevant memory...")
    results = manager.get_relevant_memory(
        topic,
        limit=5,
    )

    print("\n=== RELEVANT MEMORY ===")
    print(results)

    if results is None:
        raise AssertionError(
            "MemoryManager returned no result."
        )

    print("\nRetrieving previous discussion...")

    previous = manager.check_previous_discussion(
        topic,
        limit=5,
    )

    print("\n=== PREVIOUS DISCUSSION ===")
    print(previous)

    if previous is None:
        raise AssertionError(
            "Previous discussion check returned no result."
        )

    print("\nMEMORY MANAGER TEST PASSED")

    manager.close()


if __name__ == "__main__":
    main()