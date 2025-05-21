import feedparser
from bs4 import BeautifulSoup
import requests
import os

LAST_NEWS_FILE = "last_news_id.txt"
FEEDS = [
    "https://www.investing.com/rss/news_301.rss",        # اقتصاد جهان
    "https://feeds.bbci.co.uk/persian/rss.xml",           # بی‌بی‌سی فارسی
]

def get_and_analyze_news():
    last_id = read_last_news_id()
    news_texts = []

    for url in FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries[:5]:
            if entry.id == last_id:
                break
            title = entry.title
            summary = BeautifulSoup(entry.summary, "html.parser").text.strip()
            link = entry.link
            text = f"{title}\n{summary}\n{link}"
            news_texts.append(text)

    if news_texts:
        write_last_news_id(feed.entries[0].id)

    impact = "🔍 تحلیل اخبار:\n"
    for text in news_texts:
        impact += f"• {text.splitlines()[0]}\n"

    return impact if news_texts else "هیچ خبر جدید مهمی یافت نشد."

def read_last_news_id():
    if not os.path.exists(LAST_NEWS_FILE):
        return ""
    with open(LAST_NEWS_FILE, "r") as f:
        return f.read().strip()

def write_last_news_id(news_id):
    with open(LAST_NEWS_FILE, "w") as f:
        f.write(news_id)
