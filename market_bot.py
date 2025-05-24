
from local_prices import get_local_market
from telegram_sender import send_telegram_message
from message_guard import is_new_message

if __name__ == "__main__":
    message = "💰 قیمت‌های لحظه‌ای بازار ایران:

" + get_local_market() + "

تحلیل و گردآوری: Masoudgoldx"
    if is_new_message("market_" + message):
        send_telegram_message(message)
