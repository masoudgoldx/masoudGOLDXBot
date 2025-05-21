import requests

def get_news():
    # اینجا فعلاً فقط یک متن تست ساده می‌ذارم
    return "این یک پیام تست است. اگر این پیام را دریافت کردی یعنی بات درست کار می‌کند."

def send_tg_message(message):
    url = "https://api.telegram.org/bot7352244492:AAGOrkQXT88z1OH975q09jWkBcoI3G3ifEQ/sendMessage"
    payload = {
        "chat_id": "-1002586854094",
        "message_thread_id": 2,
        "text": message
    }
    requests.post(url, data=payload)

if name == "__main__":
    news = get_news()
    send_tg_message(news)
