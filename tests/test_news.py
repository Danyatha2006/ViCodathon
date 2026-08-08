from automation.discovery.news_fetcher import fetch_latest_news


def test_news_fetcher_returns_list():
    articles = fetch_latest_news()

    assert isinstance(articles, list)


def test_news_articles_have_required_fields():
    articles = fetch_latest_news()

    for article in articles:
        assert "title" in article
        assert "url" in article
        assert "source" in article
        assert "id" in article