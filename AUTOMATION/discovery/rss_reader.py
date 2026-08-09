import feedparser

from AUTOMATION.discovery.source_manager import get_sources


def read_rss_feed(feed_url):
    """
    Read articles from an RSS feed.
    Returns a list of articles.
    """

    feed = feedparser.parse(feed_url)

    articles = []

    for entry in feed.entries:
        article = {
            "title": entry.get("title", ""),
            "url": entry.get("link", ""),
            "summary": entry.get("summary", ""),
            "published": entry.get("published", "")
        }

        articles.append(article)

    return articles


def collect_from_all_sources():
    """Collect articles from all configured RSS sources."""

    all_articles = []

    sources = get_sources()

    for source_name, feed_url in sources.items():
        print(f"Fetching: {source_name}")

        articles = read_rss_feed(feed_url)

        for article in articles:
            article["source"] = source_name

        all_articles.extend(articles)

    return all_articles


if __name__ == "__main__":
    print("Starting news collection...\n")

    articles = collect_from_all_sources()

    print(f"\nTotal articles found: {len(articles)}\n")

    for article in articles[:5]:
        print("TITLE:", article["title"])
        print("SOURCE:", article["source"])
        print("URL:", article["url"])
        print()