import requests
import feedparser
from bs4 import BeautifulSoup

LAST_NEWS_FILE = "last_news_id.txt"
TELEGRAM_API_URL = "https://api.telegram.org/bot7352244492:AAGOrkQXT88z1OH975q09jWkBcoI3G3ifEQ/sendMessage"
CHAT_ID = "-1002586854094"
THREAD_ID = 2

def get_news():
    feeds = [
        ("https://www.investing.com/rss/news_301.rss", "Investing"),
        ("https://feeds.feedburner.com/CoinDesk", "Coindesk")
    ]
    news_items = []
    for url, source in feeds:
        feed = feedparser.parse(url)
        for entry in feed.entries[:2]:
            title = entry.title
            summary = BeautifulSoup(entry.summary, "html.parser").text.strip() if hasattr(entry, "summary") else "تحلیل مشخصی برای این خبر ارائه نشده."
            link = entry.link
            news_items.append({
                "title": title,
                "summary": summary,
                "link": link,
                "source": source
            })
    return news_items

def read_last_news_link():
    try:
        with open(LAST_NEWS_FILE, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return ""

def write_last_news_link(link):
    with open(LAST_NEWS_FILE, "w") as f:
        f.write(link)

def send_telegram_message(message):
    payload = {
        "chat_id": CHAT_ID,
        "message_thread_id": THREAD_ID,
        "text": message
    }
    response = requests.post(TELEGRAM_API_URL, data=payload)
    return response.status_code == 200

def process_and_send_news():
    news_items = get_news()
    last_link = read_last_news_link()
    for item in news_items:
        if item["link"] == last_link:
            continue  # پیام تکراری نفرسته

        message = (
            f"[خبر اقتصادی جدید از {item['source']}]\n"
            f"عنوان: {item['title']}\n"
            f"تحلیل: {item['summary']}\n"
            f"لینک: {item['link']}"
        )
        if send_telegram_message(message):
            write_last_news_link(item["link"])
            break  # فقط یک خبر بفرسته

process_and_send_news()