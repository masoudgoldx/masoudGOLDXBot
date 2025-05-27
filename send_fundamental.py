from telegram_sender import send_message
from datetime import datetime

def get_news():
    today = datetime.now().strftime("%Y/%m/%d – %H:%M")
    return f"""📰 اخبار اقتصادی مهم – {today}
🌍 جهانی:
– افزایش نرخ بهره آمریکا
– نشست G7 درباره تورم

🗺️ منطقه‌ای:
– نوسان قیمت نفت در خاورمیانه
– تنش در مرز روسیه و اروپا
━━━━━━━━━━━━━━━"""

if __name__ == "__main__":
    send_message(get_news())
