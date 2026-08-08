from ai.memory.breeth_client import BreethMemoryClient


def main():

    print("\n=== BREETH MEMORY STORAGE TEST ===")

    client = BreethMemoryClient()

    memory_data = {
        "agent_name": "AURA",
        "persona": "AI Security Researcher",
        "topic": "Indirect Prompt Injection in Autonomous AI Agents",
        "summary": (
            "A newly identified prompt injection technique allows "
            "malicious content to manipulate autonomous AI agents "
            "into overriding safety instructions."
        ),
        "generated_post": (
            "A newly identified prompt injection technique shows how "
            "malicious content can manipulate autonomous AI agents "
            "into bypassing safety controls."
        ),
        "rationale": (
            "The topic is highly relevant to AI security and directly "
            "matches AURA's editorial mission."
        ),
        "sources": [],
        "timestamp": "2026-08-08T14:00:00",
    }

    print("Storing memory...")

    result = client.store_memory(memory_data)

    print("\nBreeth response:")
    print(result)

    print("\nBREETH MEMORY STORAGE TEST PASSED")

    client.close()


if __name__ == "__main__":
    main()