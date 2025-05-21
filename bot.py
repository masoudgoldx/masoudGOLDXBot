import requests
import feedparser

BOT_TOKEN = "7352244492:AAGOrkQXT88z1OH975q09jWkBcoI3G3ifEQ"
CHAT_ID = "-1002586854094"
THREAD_ID = 2

SOURCES = [
    ("Investing", "https://www.investing.com/rss/news_285.rss"),
    ("Bloomberg", "https://www.bloomberg.com/feed/podcast/etf-report.xml"),
    ("Reuters", "https://feeds.reuters.com/reuters/businessNews"),
    ("Coindesk", "https://www.coindesk.com/arc/outboundfeeds/rss/"),
    # هر منبع فاندای مهم دیگه‌ای خواستی اضافه کن
]

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
            title = entry.title
            summary = entry.summary if hasattr(entry, 'summary') else ""
            link = entry.link
            if news_id == last_id:
                continue  # پیام تکراری نیست
            msg = f"""[خبر جدید از {name}]
عنوان: {title}
خلاصه: {summary}
لینک: {link}
"""
            with open("last_news_id.txt", "w") as f:
                f.write(news_id)
            return msg
        except Exception as e:
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
    news = get_latest_news()
    if news:
        send_telegram_message(news)
