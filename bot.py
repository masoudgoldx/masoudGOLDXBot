
import requests
import feedparser

BOT_TOKEN = "7352244492:AAGOrkQXT88z1OH975q09jWkBcoI3G3ifEQ"
CHAT_ID = "-1002586854094"
THREAD_ID = 2

RSS_FEEDS = [
    "https://www.forexfactory.com/ffcal_week_this.xml",
    "https://www.investing.com/rss/news_25.rss"
]

def fetch_latest_news():
    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries[:5]:
            yield {
                "title": entry.title,
                "link": entry.link,
                "published": entry.published if hasattr(entry, 'published') else "",
            }

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "message_thread_id": THREAD_ID,
        "text": text,
        "disable_web_page_preview": True
    }
    resp = requests.post(url, data=payload)
    print(resp.status_code, resp.text)

def main():
    news_list = list(fetch_latest_news())
    if not news_list:
        print("خبر جدیدی نیست.")
        return

    latest = news_list[0]
    message = (
        f"📢 [خبر اقتصادی جدید]\n"
        f"عنوان: {latest['title']}\n"
        f"تاریخ: {latest['published']}\n"
        f"لینک: {latest['link']}"
    )
    send_message(message)

if name == "__main__":
    main()
