import os
import re
import feedparser
import requests
from bs4 import BeautifulSoup

# فایل ذخیره آخرین خبر پردازش‌شده
LAST_NEWS_FILE = "last_news_id.txt"

# دریافت مقادیر از محیط (برای تلگرام)
TELEGRAM_API_URL = os.getenv("TELEGRAM_TOKEN")
THREAD_ID = os.getenv("CHAT_ID")

def escape_markdown(text):
    """
    کاراکترهای خاص Markdown را برای ارسال به تلگرام escape می‌کند.
    """
    return re.sub(r'([_*[\]()~`>#+\-=|{}.!])', r'\\\1', text)

def load_last_news_id():
    """
    خواندن ID آخرین خبر پردازش‌شده از فایل محلی.
    """
    if os.path.exists(LAST_NEWS_FILE):
        with open(LAST_NEWS_FILE, "r", encoding="utf-8") as f:
            return f.read().strip()
    return None

def save_last_news_id(news_id):
    """
    ذخیره آخرین ID خبر پردازش‌شده.
    """
    with open(LAST_NEWS_FILE, "w", encoding="utf-8") as f:
        f.write(news_id)

def get_and_analyze_news():
    """
    خواندن فیدهای خبری RSS و استخراج اخبار جدید.
    """
    feeds = [
        ("https://www.investing.com/rss/news_301.rss", "Investing"),
        ("https://feeds.feedburner.com/coindesk", "CoinDesk"),
    ]

    news_items = []
    last_id = load_last_news_id()

    for url, source in feeds:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            if not hasattr(entry, "id"):
                continue
            if entry.id == last_id:
                break  # از اینجا به بعد تکراریه

            title = entry.title
            summary = BeautifulSoup(entry.summary, "html.parser").text.strip() if hasattr(entry, "summary") else "بدون خلاصه"
            link = entry.link

            news_items.append({
                "title": title,
                "summary": summary,
                "link": link,
                "source": source
            })

        # فقط ID اولین خبر رو ذخیره کن (آخرین خبر منتشرشده)
        if feed.entries and hasattr(feed.entries[0], "id"):
            save_last_news_id(feed.entries[0].id)

    return news_items

def send_to_telegram(news_items):
    """
    ارسال اخبار با فرمت Markdown به تلگرام.
    """
    if not TELEGRAM_API_URL or not THREAD_ID:
        raise EnvironmentError("مقادیر محیطی TELEGRAM_TOKEN و CHAT_ID تعریف نشده‌اند.")

    for item in news_items:
        msg = (
            f"*{escape_markdown(item['title'])}*\n"
            f"{escape_markdown(item['summary'])}\n"
            f"منبع: {item['source']}\n"
            f"{item['link']}"
        )
        data = {
            "chat_id": THREAD_ID,
            "text": msg,
            "parse_mode": "Markdown"
        }
        response = requests.post(TELEGRAM_API_URL, data=data)
        if not response.ok:
            print(f"خطا در ارسال پیام:\n{response.text}")
