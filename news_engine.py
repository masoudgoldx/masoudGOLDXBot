import feedparser
import requests
from bs4 import BeautifulSoup
import os

LAST_NEWS_FILE = "last_news_id.txt"
TELEGRAM_API_URL = os.getenv("TELEGRAM_TOKEN")
THREAD_ID = os.getenv("CHAT_ID")

def get_and_analyze_news():
    feeds = [
        ("https://www.investing.com/rss/news_301.rss", "Investing"),
        ("https://feeds.feedburner.com/coindesk", "CoinDesk"),
    ]

    news_items = []

    last_id = None
    if os.path.exists(LAST_NEWS_FILE):
        with open(LAST_NEWS_FILE, "r") as f:
            last_id = f.read().strip()

    for url, source in feeds:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            if not hasattr(entry, "id"):
                continue
            if entry.id == last_id:
                break

            title = entry.title
            summary = BeautifulSoup(entry.summary, "html.parser").text.strip() if hasattr(entry, "summary") else "بدون خلاصه"
            link = entry.link

            news_items.append({
                "title": title,
                "summary": summary,
                "link": link,
                "source": source
            })

        if feed.entries and hasattr(feed.entries[0], "id"):
            with open(LAST_NEWS_FILE, "w") as f:
                f.write(feed.entries[0].id)

    return news_items

def send_to_telegram(news_items):
    for item in news_items:
        msg = f"**{item['title']}**\n{item['summary']}\nمنبع: {item['source']}\n{item['link']}"
        data = {
            "chat_id": THREAD_ID,
            "text": msg,
            "parse_mode": "Markdown"
        }
        requests.post(TELEGRAM_API_URL, data=data)
