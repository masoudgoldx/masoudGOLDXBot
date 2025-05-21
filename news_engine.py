
import feedparser
from bs4 import BeautifulSoup

domestic_feeds = [
    ("https://www.irna.ir/rss", "IRNA"),
    ("https://www.mehrnews.com/rss", "MEHR"),
    ("https://www.farsnews.ir/rss", "FARS")
]

international_feeds = [
    ("https://feeds.reuters.com/reuters/businessNews", "Reuters"),
    ("https://www.investing.com/rss/news_301.rss", "Investing"),
    ("https://feeds.feedburner.com/CoinDesk", "Coindesk")
]

keywords = ["تحریم", "تورم", "نرخ بهره", "دلار", "طلا", "سکه", "برجام", "بورس", "عرضه ارز"]

def get_and_analyze_news():
    messages = []

    for url, source in domestic_feeds + international_feeds:
        feed = feedparser.parse(url)
        for entry in feed.entries[:2]:
            title = BeautifulSoup(entry.title, "html.parser").text
            summary = BeautifulSoup(entry.get("summary", ""), "html.parser").text.strip()
            impact = "بی‌تأثیر"
            for key in keywords:
                if key in title or key in summary:
                    impact = f"اثرگذار بر بازار (کلیدواژه: {key})"
                    break
            messages.append(f"[{source}]\n{title}\n{summary}\nتحلیل: {impact}\n")

    return "\n".join(messages)
