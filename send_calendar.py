from telegram_sender import send_message
from datetime import datetime

def get_calendar():
    today = datetime.now().strftime("%Y/%m/%d")
    return f"📅 تقویم اقتصادی امروز – {today}\n\n🔥 USD – درآمدزایی بخش خدمات (16:00)\n⚠️ EUR – شاخص تورم (12:30)\n━━━━━━━━━━━━━━━"

if __name__ == "__main__":
    msg = get_calendar()
    send_message(msg)
