
import feedparser
from telegram_sender import send_telegram_message
from message_guard import is_new_message
from news_formatter import format_news_item

if __name__ == "__main__":
    feed = feedparser.parse("https://www.investing.com/rss/news_25.rss")
    messages = []

    for entry in feed.entries[:5]:
        title = getattr(entry, "title", "")
        summary = getattr(entry, "summary", "")
        link = getattr(entry, "link", "")
        source = getattr(entry, "source", {}).get("title", "Investing")

        msg = format_news_item(title, summary, source, link)
        if is_new_message(msg):
            messages.append(msg)

    for message in messages:
        send_telegram_message(message)
