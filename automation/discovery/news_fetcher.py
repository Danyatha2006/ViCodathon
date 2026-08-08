from automation.discovery.rss_reader import collect_from_all_sources
from automation.discovery.duplicate_detector import remove_duplicates


def fetch_latest_news():
    """
    Fetch the latest news from all configured sources.
    """

    articles = collect_from_all_sources()

    cleaned_articles = []

    for article in articles:
        title = article.get("title", "").strip()
        url = article.get("url", "").strip()

        # Ignore articles without a title or URL
        if not title or not url:
            continue

        cleaned_article = {
            "title": title,
            "url": url,
            "summary": article.get("summary", "").strip(),
            "published": article.get("published", ""),
            "source": article.get("source", "")
        }

        cleaned_articles.append(cleaned_article)

    return remove_duplicates(cleaned_articles)


if __name__ == "__main__":
    print("Fetching latest news...\n")

    articles = fetch_latest_news()

    print(f"Usable unique articles: {len(articles)}\n")

    for article in articles[:5]:
        print("TITLE:", article["title"])
        print("SOURCE:", article["source"])
        print("ID:", article["article_id"])
        print("URL:", article["url"])
        print()