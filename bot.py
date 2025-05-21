import requests

def get_news():
    # اینجا خبر یا پیام واقعی رو بساز (الان فقط برای تست یک متن ساده گذاشتم)
    news = "این یک خبر واقعی تستی است (برای بررسی ضد تکرار)"
    return news

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
    url = "https://api.telegram.org/bot7352244492:AAGOrkQXT88z1OH975q09jWkBcoI3G3ifEQ/sendMessage"
    payload = {
        "chat_id": "-1002586854094",
        "message_thread_id": 2,  # اگر گروهت سوپرجروپ با تاپیک است، این خط باشه. اگر فقط گروه معمولی، حذف کن.
        "text": message
    }
    requests.post(url, data=payload)

if name == "__main__":
    news = get_news()
    last_news = read_last_news()
    if news.strip() != "":
        send_telegram_message(news)
        write_last_news(news)
