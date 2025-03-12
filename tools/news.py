import feedparser
import re


def get_news(query: str) -> str:
    query = re.sub(r"\s+", "+", query)

    url = f"https://news.google.com/rss/search?q={query}&hl=en-US&gl=US&ceid=US:en"

    feed = feedparser.parse(url)

    news_items = []

    for entry in feed.entries[:3]:
        title = entry.title

        link = entry.link

        title = re.sub(r"\s+-\s+.*$", "", title)

        news_items.append(f"• {title}\n  {link}")

    return "\n\n".join(news_items) if news_items else "No news found for this query."