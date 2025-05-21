Masoud Msv, [5/21/2025 5:20 AM]
import requests

url = "https://api.telegram.org/bot7352244492:AAGOrkQXT88z1OH975q09jWkBcoI3G3ifEQ/sendMessage"

payload = {
    "chat_id": "-1002586854094",
    "message_thread_id": 2,
    "text": "✅ تست موفق! MasoudGoldXBot فعال شد و آماده ارسال اخبار فاندامنتال است."
}

requests.post(url, data=payload)

Masoud Msv, [5/21/2025 6:20 AM]
import requests
import time

# اطلاعات توکن و چت آیدی
BOT_TOKEN = "توکن رباتت اینجا"
CHAT_ID = "آیدی گروه یا چت اینجا"

# پیام تست اولیه
message = "MasoudGOLDXBot فعال شد. تحلیل واقعی از درون آغاز می‌شود، نه از چارت."

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": message
}

try:
    requests.post(url, data=payload)
except Exception as e:
    print("خطا:", e)
