RSS_SOURCES = {
    "ars_technica_ai": "https://arstechnica.com/ai/feed/",
}


def get_sources():
    """Return the configured RSS sources."""
    return RSS_SOURCES.copy()


def add_source(name, url):
    """Add a new RSS source."""
    RSS_SOURCES[name] = url


def remove_source(name):
    """Remove an RSS source if it exists."""
    RSS_SOURCES.pop(name, None)