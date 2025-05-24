
import os
from news_engine import get_and_analyze_news
from tech_analysis import get_technical_analysis
from local_prices import get_local_market
from economic_calendar import get_economic_calendar
from message_builder import build_message
from telegram_sender import send_telegram_message
from message_guard import is_new_message

if __name__ == "__main__":
    news = get_and_analyze_news()
    tech = get_technical_analysis()
    local = get_local_market()
    calendar = get_economic_calendar()

    message = build_message(news, tech, local, calendar)

    if not is_new_message(message):
        print("⛔ پیام تکراری است. ارسال نمی‌شود.")
        exit()

    send_telegram_message(message)
