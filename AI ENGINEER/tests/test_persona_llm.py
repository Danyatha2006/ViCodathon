from ai.models.llm_client import LLMClient
from ai.persona.persona import AURAPersona


def main():
    persona = AURAPersona()
    llm = LLMClient()

    prompt = f"""
{persona.get_system_prompt()}

TASK:

Analyze this topic as AURA:

"Researchers discovered a new prompt injection technique
that can manipulate AI agents into following malicious
instructions."

Explain:

1. What happened
2. Why it matters for AI security
3. Whether AURA should consider this topic important

Do not write a social media post yet.
"""

    response = llm.generate(prompt)

    print("\nAURA RESPONSE")
    print("=============")
    print(response)


if __name__ == "__main__":
    main()