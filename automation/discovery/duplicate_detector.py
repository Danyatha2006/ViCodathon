import hashlib


def generate_article_id(article):
    """
    Generate a unique ID for an article based on its URL.
    """

    url = article.get("url", "").strip()

    if not url:
        return None

    return hashlib.sha256(url.encode("utf-8")).hexdigest()


def remove_duplicates(articles):
    """
    Remove duplicate articles from a list.
    """

    seen_ids = set()
    unique_articles = []

    for article in articles:
        article_id = generate_article_id(article)

        if article_id is None:
            continue

        if article_id in seen_ids:
            continue

        seen_ids.add(article_id)

        article["article_id"] = article_id
        unique_articles.append(article)

    return unique_articles
if __name__ == "__main__":
    test_articles = [
        {
            "title": "AI Model Released",
            "url": "https://example.com/article1"
        },
        {
            "title": "AI Model Released",
            "url": "https://example.com/article1"
        },
        {
            "title": "New AI Chip",
            "url": "https://example.com/article2"
        }
    ]

    unique_articles = remove_duplicates(test_articles)

    print("Original articles:", len(test_articles))
    print("Unique articles:", len(unique_articles))

    for article in unique_articles:
        print(article["title"])
        print(article["article_id"])
        print()