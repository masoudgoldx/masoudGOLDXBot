
from economic_calendar import get_economic_calendar
from telegram_sender import send_telegram_message
from message_guard import is_new_message

if __name__ == "__main__":
    calendar = get_economic_calendar()
    message = f"📆 تقویم اقتصادی امروز:

{calendar}

تحلیل و گردآوری: Masoudgoldx"
    if is_new_message("calendar_" + message):
        send_telegram_message(message)
