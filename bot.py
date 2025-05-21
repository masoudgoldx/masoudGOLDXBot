import requests

def send_telegram_message(message):
    url = "https://api.telegram.org/bot7352244492:AAGOrkQXT88z1OH975q09jWkBcoI3G3ifEQ/sendMessage"
    payload = {
        "chat_id": "-1002586854094",
        "message_thread_id": 2,
        "text": message
    }
    requests.post(url, data=payload)

if name == "__main__":
    message = "تست ارسال پیام با MasoudGOLDXBot (غیرتکراری)"
    send_telegram_message(message)
