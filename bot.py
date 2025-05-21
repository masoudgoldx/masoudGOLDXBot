import requests
import feedparser
from bs4 import BeautifulSoup

def get_news():
    feeds = [
        "https://www.investing.com/rss/news_301.rss",   # Investing
        "https://feeds.feedburner.com/CoinDesk"         # Coindesk
    ]
    all_news = ""
    for url in feeds:
        feed = feedparser.parse(url)
        for entry in feed.entries[:2]:
            title = entry.title
            summary = BeautifulSoup(entry.summary, 'html.parser').text.strip() if hasattr(entry, "summary") else "تحلیل مشخصی برای این خبر ارائه نشده."
            link = entry.link
            source = "Investing" if "investing" in url else "Coindesk"
            all_news += f"[خبر اقتصادی جدید از {source}]\nعنوان: {title}\nتحلیل: {summary}\nلینک: {link}\n\n"
    return all_news.strip()

def read_last_news():
    try:
        with open('last_news_id.txt', 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        return ""

def write_last_news(news):
    with open('last_news_id.txt', 'w') as f:
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
    news = get_news()
    last_news = read_last_news()
    if news != last_news:
        send_telegram_message(news)
        write_last_news(news)
