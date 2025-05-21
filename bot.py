import requests
from tech_analysis import get_analysis

def get_news():
    # این قسمت رو بعداً با خبر واقعی جایگزین می‌کنی
    fundamental = "خبر فاندامنتال جدید"  # این خط تست است
    analysis = get_analysis()  # خروجی تحلیل تکنیکال
    return f"{fundamental}\n{analysis}"

def read_last_news():
    try:
        with open('last_news_id.txt', 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        return ""

def write_last_news(news):
    with open('last_news_id.txt', 'w') as f:
        f.write(news)

def send_telegram_message(message):
    url = "https://api.telegram.org/bot<توکن_ربات>/sendMessage"
    payload = {
        "chat_id": "<chat_id>",
        "text": message
    }
    requests.post(url, data=payload)

if name == "__main__":
    news = get_news()
    last_news = read_last_news()
    if news != last_news and news.strip() != "":
        send_telegram_message(news)
        write_last_news(news)
