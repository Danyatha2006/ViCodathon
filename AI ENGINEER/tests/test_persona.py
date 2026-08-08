from ai.persona.persona import AURAPersona


def main():
    persona = AURAPersona()

    print("\nAURA PERSONA")
    print("============")

    profile = persona.get_profile()

    print(f"Name: {profile['name']}")
    print(f"Role: {profile['role']}")
    print(f"Domain: {profile['domain']}")
    print(f"Mission: {profile['mission']}")

    print("\nSystem Prompt")
    print("-------------")
    print(persona.get_system_prompt())


if __name__ == "__main__":
    main()