import requests

def get_news():
    # ... کد دریافت خبر از سایت خارجی مثل دیروز ...
    # فرض کن خروجی تابع یک رشته خبر جدیده و اگر تکراری باشه خروجی '' برمی‌گرده
    # مثلا:
    latest_news = "خبر جدید اقتصادی ..."
    return latest_news

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
        "chat_id": "-1002586854094",  # آی‌دی گروه شما
        "message_thread_id": 2,        # آیدی تاپیک
        "text": message
    }
    requests.post(url, data=payload)

if __name__ == "__main__":
    news = get_news()
    last_news = read_last_news()
    if news and news != last_news:
        send_telegram_message(news)
        write_last_news(news)
