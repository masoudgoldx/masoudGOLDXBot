import requests

def main():
    url = "https://api.telegram.org/bot7352244492:AAGOrkQXT88z1OH975q09jWkBcoI3G3ifEQ/sendMessage"
    payload = {
        "chat_id": "-1002586854094",   # آیدی گروه با منفی
        "message_thread_id": 2,         # آیدی تاپیک (در صورت نیاز تغییر بده)
        "text": "✅ تست موفق! MasoudGoldXBot فعال شد و آماده ارسال اخبار فاندامنتال است."
    }
    requests.post(url, data=payload)

if name == "__main__":
    main()
