from news_engine import get_and_analyze_news
from tech_analysis import get_technical_analysis
import requests
import os

TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
THREAD_ID = os.environ.get("THREAD_ID")

def send_to_telegram(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "message_thread_id": int(THREAD_ID),
        "text": msg
    }
    requests.post(url, data=data)

if __name__ == "__main__":
    news = get_and_analyze_news()
    msg = "اخبار اقتصادی جدید:\n\n"
    for item in news:
        msg += f"[{item['source']}]\n{item['title']}\n{item['summary']}\nتحلیل: {item['directions']}\n\n"

    msg += "\n" + get_technical_analysis()
    send_to_telegram(msg)
