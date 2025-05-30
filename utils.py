import os
import requests

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
THREAD_ID = os.getenv("THREAD_ID")

def send_telegram_message(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": msg,
        "message_thread_id": int(THREAD_ID) if THREAD_ID else None
    }
    requests.post(url, data=data)

def load_last_message():
    try:
        with open("last_message.txt", "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        return ""

def save_last_message(msg):
    with open("last_message.txt", "w", encoding="utf-8") as f:
        f.write(msg.strip())