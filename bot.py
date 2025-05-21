import requests
from datetime import datetime

# اطلاعات اصلی
BOT_TOKEN = "7352244492:AAGOrkQXT88z1OH975q09jWkBcoI3G3ifEQ"
CHAT_ID = "-1002586854094"
THREAD_ID = 2  # شناسه تاپیک گروه

# نمونه ساختار پیام برای شبیه‌سازی پیام واقعی از سایت‌های معتبر
news_item = {
    "title": "داده‌های تورم آمریکا منتشر شد",
    "analysis": "تورم بالاتر از پیش‌بینی‌هاست که ممکن است باعث ادامه سیاست‌های انقباضی فدرال رزرو شود.",
    "impact": {
        "طلا": "صعودی",
        "یورو": "کاهشی",
        "بیت‌کوین": "بی‌ثبات",
        "نفت": "تقویت",
        "نقره": "تقویت"
    }
}

# ساخت پیام نهایی برای تلگرام
message = "📢 [خبر اقتصادی جدید]\n"
message += f"عنوان: {news_item['title']}\n"
message += f"تحلیل: {news_item['analysis']}\n"
message += "تأثیر:\n"
for asset, effect in news_item["impact"].items():
    message += f"- {asset}: {effect}\n"

# ارسال پیام
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "message_thread_id": THREAD_ID,
    "text": message.strip()
}

response = requests.post(url, data=payload)
print("Status:", response.status_code)
print("Response:", response.text)
