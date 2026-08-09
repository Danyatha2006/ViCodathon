from ai.memory.breeth_client import BreethMemoryClient


def main():
    print("\n=== BREETH CONNECTION TEST ===")

    client = BreethMemoryClient()

    print("Connecting to Breeth...")

    connected = client.connect_breeth()

    if not connected:
        raise RuntimeError("Breeth connection failed.")

    print("Breeth connection successful.")
    print("\nBREETH CONNECTION TEST PASSED")

    client.close()


if __name__ == "__main__":
    main()