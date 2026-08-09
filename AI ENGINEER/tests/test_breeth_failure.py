from ai.memory.memory_manager import MemoryManager


class FailingBreethClient:
    """Fake Breeth client used to test failure handling."""

    def retrieve_memory(self, query, limit=5):
        raise RuntimeError("Simulated Breeth unavailable")

    def search_similar_topics(self, topic, limit=5):
        raise RuntimeError("Simulated Breeth unavailable")

    def store_memory(self, memory_data):
        raise RuntimeError("Simulated Breeth unavailable")

    def close(self):
        pass


def main():

    print("\n=== BREETH FAILURE HANDLING TEST ===")

    failing_client = FailingBreethClient()

    manager = MemoryManager(
        breeth_client=failing_client
    )

    print("\nSimulating Breeth failure...")

    try:
        manager.get_relevant_memory(
            "Prompt injection in AI agents"
        )

    except RuntimeError as exc:

        print("\nExpected error caught:")
        print(exc)

        print("\nBREETH FAILURE HANDLING TEST PASSED")
        return

    raise AssertionError(
        "Breeth failure should have raised RuntimeError."
    )


if __name__ == "__main__":
    main()