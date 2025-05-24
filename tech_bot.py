
from tech_analysis import get_technical_analysis
from telegram_sender import send_telegram_message
from message_guard import is_new_message

if __name__ == "__main__":
    message = "📈 تحلیل تکنیکال:

" + get_technical_analysis() + "

تحلیل و گردآوری: Masoudgoldx"
    if is_new_message("tech_" + message):
        send_telegram_message(message)
