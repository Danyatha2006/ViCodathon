from ai.memory.breeth_client import BreethMemoryClient


def main():

    print("\n=== BREETH MEMORY RETRIEVAL TEST ===")

    client = BreethMemoryClient()

    query = "Indirect Prompt Injection in Autonomous AI Agents"

    print("\nSearching Breeth for:")
    print(query)

    results = client.retrieve_memory(
        query,
        limit=5,
    )

    print("\n=== RETRIEVAL RESULTS ===")
    print(results)

    if results is None:
        raise AssertionError(
            "Breeth returned no retrieval response."
        )

    print("\nBREETH MEMORY RETRIEVAL TEST PASSED")

    client.close()


if __name__ == "__main__":
    main()