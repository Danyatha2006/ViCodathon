from AUTOMATION.discovery.news_fetcher import fetch_latest_news


def run_agent():
    """
    Run the autonomous news collection workflow.
    """

    print("\n===== AURA AUTONOMOUS AGENT =====")
    print("Starting autonomous workflow...")

    articles = fetch_latest_news()

    print(f"Autonomous workflow completed.")
    print(f"New articles found: {len(articles)}")

    return articles


if __name__ == "__main__":
    run_agent()