import os
from dotenv import load_dotenv


def main():
    print("\n" + "=" * 70)
    print("PHASE 10.2 — ENVIRONMENT CONFIGURATION TEST")
    print("=" * 70)

    load_dotenv()

    required_variables = [
        "GEMINI_API_KEY",
        "BREETH_API_KEY",
    ]

    print("\nChecking required environment variables...")

    for variable in required_variables:
        value = os.getenv(variable)

        if not value:
            raise AssertionError(
                f"{variable} is not configured."
            )

        print(f"✓ {variable} configured")

    print("\nAPI keys detected successfully.")
    print("Actual secret values were NOT displayed.")

    print("\n" + "=" * 70)
    print("PHASE 10.2 ENVIRONMENT TEST PASSED")
    print("=" * 70)


if __name__ == "__main__":
    main()