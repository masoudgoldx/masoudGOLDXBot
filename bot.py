import requests
from news_engine import get_and_analyze_news
from tech_analysis import get_technical_analysis

def send_telegram_message(message):
    import os
    token = os.getenv("BOT_TOKEN")
    chat_id = os.getenv("CHAT_ID")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    requests.post(url, data=data)

if __name__ == "__main__":
    fundamental = get_and_analyze_news()
    technical = get_technical_analysis()

    if fundamental:
        message = "اخبار فاندامنتال:
" + "\n\n".join(
            [f"{item['title']}\n{item['summary']}\n{item['link']}" for item in fundamental]
        )
    else:
        message = "فعلاً خبر فاندامنتال جدیدی در دسترس نیست."

    message += "\n\n" + technical

    send_telegram_message(message)
