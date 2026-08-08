from ai.models.llm_client import LLMClient
from ai.models.response_parser import TopicAnalysisResponse


def main():
    llm = LLMClient()

    prompt = """
You are analyzing a technology topic for AURA,
an AI Security Researcher.

Analyze this topic:

"Researchers discovered a new prompt injection technique
that can manipulate AI agents into following malicious instructions."

Return the analysis using the required structured format.
"""

    try:
        result = llm.generate_structured(
            prompt,
            TopicAnalysisResponse,
        )

    except RuntimeError as exc:
        if "quota exhausted" in str(exc).lower():
            print("\nSTRUCTURED OUTPUT TEST SKIPPED")
            print("------------------------------")
            print("Reason: Gemini API quota exhausted.")
            print("The structured-output implementation was not changed.")
            return

        raise

    print("\nSTRUCTURED RESPONSE")
    print("-------------------")
    print(f"Topic: {result.topic}")
    print(f"Summary: {result.summary}")
    print(f"Relevance: {result.relevance_score}")
    print(f"Novelty: {result.novelty_score}")
    print(
        f"Security relevance: "
        f"{result.security_relevance_score}"
    )

    print("\nSTRUCTURED OUTPUT TEST PASSED")


if __name__ == "__main__":
    main()