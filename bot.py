Masoud Msv, [5/21/2025 5:20 AM]
import requests

url = "https://api.telegram.org/bot7352244492:AAGOrkQXT88z1OH975q09jWkBcoI3G3ifEQ/sendMessage"

payload = {
    "chat_id": "-1002586854094",
    "message_thread_id": 2,
    "text": "✅ تست موفق! MasoudGoldXBot فعال شد و آماده ارسال اخبار فاندامنتال است."
}

requests.post(url, data=payload)

Masoud Msv, [5/21/2025 7:03 AM]
import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": "✅ فعال شد. ربات MasoudGOLDX در حال ارسال اخبار لحظه‌ای است."
}

response = requests.post(url, data=payload)
print(response.text)
