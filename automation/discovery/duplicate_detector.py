import hashlib
import json
import os


MEMORY_FILE = os.path.join(
    os.path.dirname(__file__),
    "seen_articles.json"
)


def generate_article_id(article):
    """
    Generate a unique ID for an article based on its URL.
    """

    url = article.get("url", "").strip()

    if not url:
        return None

    return hashlib.sha256(url.encode("utf-8")).hexdigest()


def load_seen_ids():
    """
    Load previously seen article IDs from the memory file.
    """

    if not os.path.exists(MEMORY_FILE):
        return set()

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        return set(data)

    except (json.JSONDecodeError, OSError):
        return set()


def save_seen_ids(seen_ids):
    """
    Save article IDs so they are remembered between program runs.
    """

    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(sorted(seen_ids), file, indent=2)


def remove_duplicates(articles):
    """
    Remove articles that have already been seen.
    """

    seen_ids = load_seen_ids()
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

    save_seen_ids(seen_ids)

    return unique_articles