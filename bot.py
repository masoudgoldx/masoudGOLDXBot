import requests, feedparser
from bs4 import BeautifulSoup
from html import unescape

BOT_TOKEN = "7352244492:AAGOrkQXT88z1OH975q09jWkBcoI3G3ifEQ"
CHAT_ID = "-1002586854094"
THREAD_ID = 2

SOURCES = [
    ("Investing", "https://www.investing.com/rss/news_285.rss"),
    ("Bloomberg", "https://www.bloomberg.com/feed/podcast/etf-report.xml"),
    ("Reuters", "https://feeds.reuters.com/reuters/businessNews"),
    ("Coindesk", "https://www.coindesk.com/arc/outboundfeeds/rss/")
]

def analyze_news(title):
    title = title.lower()
    if "rate" in title or "interest" in title:
        return "احتمالاً این خبر روی دلار و طلا تأثیر مستقیم دارد (نرخ بهره)."
    elif "inflation" in title:
        return "خبر مربوط به تورم است، ممکن است باعث نوسان در بازار طلا شود."
    elif "war" in title or "conflict" in title:
        return "تنش یا جنگ! احتمال رشد انس جهانی زیاد است."
    elif "bitcoin" in title:
        return "خبر مربوط به بیت‌کوین است و می‌تواند بازار کریپتو را حرکت دهد."
    return "تحلیل مشخصی برای این خبر ارائه نشده."

def get_latest_news():
    try:
        with open("last_news_id.txt", "r") as f:
            last_id = f.read().strip()
    except:
        last_id = ""
    for name, url in SOURCES:
        try:
            feed = feedparser.parse(url)
            entry = feed.entries[0]
            news_id = getattr(entry, "id", entry.link)
            title = unescape(entry.title)
            link = entry.link
            if news_id == last_id:
                continue
            analysis = analyze_news(title)
            message = f"[خبر اقتصادی جدید از {name}]\nعنوان: {title}\nتحلیل: {analysis}\nلینک: {link}"
            with open("last_news_id.txt", "w") as f:
                f.write(news_id)
            return message
        except:
            continue
    return None

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "message_thread_id": THREAD_ID,
        "text": message
    }
    requests.post(url, data=payload)

if __name__ == "__main__":
    msg = get_latest_news()
    if msg:
        send_telegram_message(msg)
