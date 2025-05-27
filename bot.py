import requests
from telegram_sender import send_telegram_message
import datetime

def get_fundamental_news():
    try:
        now = datetime.datetime.now().strftime('%Y/%m/%d - %H:%M')
        news = [
            "📌 CPI آمریکا امروز منتشر می‌شود (16:00)",
            "📌 سخنرانی رئیس فدرال رزرو فردا شب خواهد بود (22:30)",
            "📌 نرخ بهره اروپا تغییری نداشت (13:15)",
        ]
        output = "🧠 <b>اخبار فاندامنتال مهم امروز</b>\n\n"
        output += "\n".join([f"🔸 {item}" for item in news])
        output += f"\n\n🕓 به‌روزرسانی: {now}"
        return output
    except Exception as e:
        return f"❌ خطا در دریافت اخبار فاندامنتال: {e}"

if __name__ == "__main__":
    message = get_fundamental_news()
    send_telegram_message(message)
