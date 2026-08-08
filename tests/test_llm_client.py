from ai.models.llm_client import LLMClient


def main():
    llm = LLMClient()

    response = llm.generate(
    "Explain prompt injection in one simple sentence."
)

    print("\nGemini response:")
    print(response)


if __name__ == "__main__":
    main()