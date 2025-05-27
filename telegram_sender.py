import requests
from config import BOT_TOKEN, CHAT_ID

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }

    response = requests.post(url, data=data)
    if response.status_code != 200:
        print("❌ خطا در ارسال پیام:", response.status_code)
        print("پاسخ سرور:", response.text)
