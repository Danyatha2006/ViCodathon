from AUTOMATION.discovery.rss_reader import collect_from_all_sources


def fetch_latest_news():
    """
    Fetch the latest news from all configured sources.

    IMPORTANT:
    This function does NOT mark articles as seen.
    Articles should only be marked as processed after
    successful AI processing/publishing.
    """

    articles = collect_from_all_sources()

    cleaned_articles = []
    seen_urls = set()

    for article in articles:
        title = article.get("title", "").strip()
        url = article.get("url", "").strip()

        if not title or not url:
            continue

        # Remove duplicates within this single RSS fetch.
        if url in seen_urls:
            continue

        seen_urls.add(url)

        cleaned_articles.append(
            {
                "title": title,
                "url": url,
                "summary": article.get("summary", "").strip(),
                "published": article.get("published", ""),
                "source": article.get("source", ""),
            }
        )

    return cleaned_articles


if __name__ == "__main__":
    print("Fetching latest news...\n")

    articles = fetch_latest_news()

    print(f"Usable unique articles: {len(articles)}\n")

    for article in articles[:5]:
        print("TITLE:", article["title"])
        print("SOURCE:", article["source"])
        print("URL:", article["url"])
        print()