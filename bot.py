import requests
from news_engine import get_and_analyze_news
from tech_analysis import get_technical_analysis

TELEGRAM_API_URL = "https://api.telegram.org/bot7352244492:AAGOrkQXT88z1OH975q09jWkBcoI3G3ifEQ/sendMessage"
CHAT_ID = "-1002586854094"
THREAD_ID = 2

def send_telegram_message(message):
    payload = {
        "chat_id": CHAT_ID,
        "message_thread_id": THREAD_ID,
        "text": message
    }
    response = requests.post(TELEGRAM_API_URL, data=payload)
    return response.status_code == 200

def format_news_message(news_data):
    msg = "اخبار اقتصادی جدید با تحلیل ساده:\n\n"
    for item in news_data:
        msg += f"منبع: {item['source']}\n"
        msg += f"عنوان: {item['title']}\n"
        msg += f"خلاصه: {item['summary']}\n"
        msg += "تأثیر احتمالی:\n"
        for asset, direction in item['directions'].items():
            msg += f"  - {asset}: {direction}\n"
        msg += "\n"
    return msg.strip()

def main():
    news_data = get_and_analyze_news()
    news_message = format_news_message(news_data)
    tech_message = get_technical_analysis()
    final_message = f"{news_message}\n\n{'-'*30}\n\n{tech_message}"
    send_telegram_message(final_message)

if __name__ == "__main__":
    main()
