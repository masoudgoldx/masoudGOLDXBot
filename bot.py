import requests
import feedparser
from bs4 import BeautifulSoup

def get_news():
    urls = [
        "https://www.investing.com/rss/news_301.rss",  # Economic News
        "https://www.coindesk.com/arc/outboundfeeds/rss/"  # Crypto News
    ]
    messages = []
    for url in urls:
        feed = feedparser.parse(url)
        for entry in feed.entries[:2]:
            title = entry.title
            link = entry.link
            source = "Investing" if "investing" in url else "Coindesk"
            message = f"[خبر اقتصادی جدید از {source}]
عنوان: {title}
تحلیل: تحلیل مشخصی برای این خبر ارائه نشده.
لینک: {link}"
            messages.append(message)
    return messages

def read_last_news():
    try:
        with open("last_news_id.txt", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return ""

def write_last_news(news):
    with open("last_news_id.txt", "w") as f:
        f.write(news)

def send_telegram_message(message):
    url = "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/sendMessage"
    payload = {
        "chat_id": "<YOUR_CHAT_ID>",
        "message_thread_id": 2,
        "text": message
    }
    requests.post(url, data=payload)

if __name__ == "__main__":
    all_news = get_news()
    last_news = read_last_news()
    for msg in all_news:
        if msg != last_news:
            send_telegram_message(msg)
            write_last_news(msg)
