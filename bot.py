import requests
import feedparser

BOT_TOKEN = "7352244492:AAGOrkQXT88z1OH975q09jWkBcoI3G3ifEQ"
CHAT_ID = "-1002586854094"
THREAD_ID = 2

FEEDS = [
    {
        "name": "Investing",
        "url": "https://www.investing.com/rss/news_25.rss",
        "emoji": "🌎"
    },
    {
        "name": "ForexFactory",
        "url": "https://www.forexfactory.com/ffcal_week_this.xml",
        "emoji": "💱"
    },
    {
        "name": "Coindesk",
        "url": "https://coindesk.com/arc/outboundfeeds/rss/",
        "emoji": "🪙"
    }
]

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "message_thread_id": THREAD_ID,
        "text": text,
        "disable_web_page_preview": True
    }
    requests.post(url, data=payload)

def fetch_and_send_latest():
    for feed in FEEDS:
        parsed = feedparser.parse(feed["url"])
        if not parsed.entries:
            msg = f"{feed['emoji']} [{feed['name']}]\nخبر جدیدی پیدا نشد."
        else:
            entry = parsed.entries[0]
            published = getattr(entry, "published", "-")
            title = getattr(entry, "title", "-")
            link = getattr(entry, "link", "-")
            msg = (
                f"{feed['emoji']} [خبر اقتصادی جدید - {feed['name']}]\n"
                f"عنوان: {title}\n"
                f"تاریخ: {published}\n"
                f"لینک: {link}"
            )
        send_message(msg)

if __name__ == "__main__":
    fetch_and_send_latest()
