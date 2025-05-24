
import os
import requests

def send_telegram_message(message):
    token = os.getenv("BOT_TOKEN")
    chat_id = os.getenv("CHAT_ID")

    if not token or not chat_id:
        print("توکن یا chat_id تنظیم نشده.")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    max_len = 4000

    for i in range(0, len(message), max_len):
        part = message[i:i+max_len]
        response = requests.post(url, data={"chat_id": chat_id, "text": part})
        print(f"Status: {response.status_code}, Response: {response.text}")
