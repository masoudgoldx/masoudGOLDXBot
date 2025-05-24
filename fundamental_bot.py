
from news_engine import get_and_analyze_news
from telegram_sender import send_telegram_message
from message_guard import is_new_message

if __name__ == "__main__":
    categorized = get_and_analyze_news()
    message = "📰 اخبار اقتصادی جهانی:

"
    for asset, items in categorized.items():
        if items:
            message += f"== {asset} ==\n"
            for item in items:
                message += f"{item['title']}\n{item['summary']}\n{item['impact']}\n{item['link']}\n\n"
    message += "تحلیل و گردآوری: Masoudgoldx"

    if is_new_message("fundamental_" + message):
        send_telegram_message(message)
