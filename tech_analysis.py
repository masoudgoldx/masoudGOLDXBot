import requests
from bs4 import BeautifulSoup
import feedparser

def get_news():
    feed_urls = [
        "https://www.investing.com/rss/news_25.rss",
        "https://www.coindesk.com/arc/outboundfeeds/rss/"
    ]
    collected = []
    for url in feed_urls:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            title = entry.title
            link = entry.link
            summary = ""
            try:
                summary = BeautifulSoup(entry.summary, 'html.parser').text.strip()
            except AttributeError:
                summary = "تحلیل مشخصی برای این خبر ارائه نشده."

            source = "Investing" if "investing" in link else "Coindesk"
            text = f"[خبر اقتصادی جدید از {source}]\nعنوان: {title}\nتحلیل: {summary}\nلینک: {link}"
            collected.append(text)
    return collected

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
    url = "https://api.telegram.org/bot7352244492:AAGOrkQXT88z1OH975q09jWkBcoI3G3ifEQ/sendMessage"
    payload = {
        "chat_id": "-1002586854094",
        "message_thread_id": 2,
        "text": message
    }
    requests.post(url, data=payload)

if __name__ == "__main__":
    all_news = get_news()
    last_sent = read_last_news()
    for item in all_news:
        if item != last_sent:
            send_telegram_message(item)
            write_last_news(item)
            break
