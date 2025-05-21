import feedparser
from bs4 import BeautifulSoup

feeds = [
    ("https://feeds.reuters.com/reuters/businessNews", "Reuters"),
    ("https://www.investing.com/rss/news_301.rss", "Investing"),
    ("https://feeds.bbci.co.uk/news/world/rss.xml", "BBC")
]

keywords = ["CPI", "interest rate", "inflation", "Fed", "ECB", "gold", "dollar", "recession"]

def get_and_analyze_news():
    messages = []
    for url, source in feeds:
        feed = feedparser.parse(url)
        for entry in feed.entries[:2]:
            title = BeautifulSoup(entry.title, "html.parser").text
            summary = BeautifulSoup(entry.get("summary", ""), "html.parser").text
            impact = "نامشخص"
            for key in keywords:
                if key.lower() in (title + summary).lower():
                    impact = f"اثرگذار (کلمه کلیدی: {key})"
                    break
            messages.append(f"[{source}]
{title}
{summary}
تحلیل: {impact}")
    return "\n\n".join(messages)