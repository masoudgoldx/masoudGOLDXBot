import os
import requests
from news_engine import get_and_analyze_news
from tech_analysis import get_technical_analysis

def send_telegram_message(message):
    token = os.getenv("BOT_TOKEN")
    chat_id = os.getenv("CHAT_ID")

    print(f"[Debug] BOT_TOKEN: {token}")
    print(f"[Debug] CHAT_ID: {chat_id}")

    if not token or not chat_id:
        print("[Error] BOT_TOKEN or CHAT_ID is not set! Please check GitHub secrets.")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    max_length = 4000  # Limit is 4096, we keep margin

    parts = [message[i:i+max_length] for i in range(0, len(message), max_length)]

    for idx, part in enumerate(parts):
        data = {
            "chat_id": chat_id,
            "text": part
        }
        response = requests.post(url, data=data)
        print(f"[Telegram] Part {idx+1}/{len(parts)} Status: {response.status_code}")
        print(f"[Telegram] Part {idx+1} Response: {response.text}")

if __name__ == "__main__":
    fundamental = get_and_analyze_news()
    technical = get_technical_analysis()

    print(f"[Debug] Fundamental: {fundamental}")
    print(f"[Debug] Technical: {technical}")

    if fundamental:
        try:
            message = "اخبار فاندامنتال:\n\n" + "\n\n".join(
                [f"{item['title']}\n{item['summary']}\n{item['link']}" for item in fundamental]
            )
        except Exception as e:
            message = f"[Error formatting fundamental]: {e}"
    else:
        message = "هیچ خبر فاندامنتالی در منابع موجود نیست."

    message += "\n\n" + technical

    if len(message.strip()) < 10:
        message = "[Test] Bot executed but no valid data found."

    send_telegram_message(message)
