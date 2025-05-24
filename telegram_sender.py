
import os
import requests

def send_telegram_message(message):
    token = os.getenv("BOT_TOKEN")
    chat_id = os.getenv("CHAT_ID")
    if not token or not chat_id:
        print("BOT_TOKEN or CHAT_ID missing")
        return
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    for i in range(0, len(message), 4000):
        part = message[i:i+4000]
        requests.post(url, data={"chat_id": chat_id, "text": part})
