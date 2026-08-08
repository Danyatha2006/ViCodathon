from ai.models.llm_client import LLMClient
from ai.models.response_parser import TopicAnalysisResponse


def test_empty_prompt():
    llm = LLMClient()

    try:
        llm.generate("")
        print("❌ Empty prompt test FAILED")
    except ValueError as error:
        print("✅ Empty prompt test PASSED")
        print(f"   Error: {error}")


def test_empty_structured_prompt():
    llm = LLMClient()

    try:
        llm.generate_structured(
            "",
            TopicAnalysisResponse,
        )
        print("❌ Empty structured prompt test FAILED")
    except ValueError as error:
        print("✅ Empty structured prompt test PASSED")
        print(f"   Error: {error}")


def main():
    print("\nAURA LLM ERROR TESTS")
    print("====================")

    test_empty_prompt()
    test_empty_structured_prompt()


if __name__ == "__main__":
    main()