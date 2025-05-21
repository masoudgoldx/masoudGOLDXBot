import requests
import datetime

# اطلاعات توکن و آیدی گروه
BOT_TOKEN = "7352244492:AAGOrkQXT88z1OH975q09jWkBcoI3G3ifEQ"
CHAT_ID = "-1002586854094"
THREAD_ID = 2  # آیدی تاپیک (topic) گروه

# لیست نمونه اخبار فرضی (شبیه‌سازی دریافت اخبار)
sample_news = [
    {
        "title": "نرخ بهره آمریکا ثابت ماند",
        "analysis": "این خبر می‌تواند فشار فروش بر دلار ایجاد کند و باعث رشد طلا و یورو شود.",
        "impact": {
            "طلا": "صعودی",
            "یورو": "تقویت",
            "بیت‌کوین": "خنثی",
            "نفت": "خنثی",
            "نقره": "صعودی"
        }
    },
    {
        "title": "افزایش تنش‌های ژئوپلیتیکی در خاورمیانه",
        "analysis": "تنش‌های ژئوپلیتیکی معمولاً باعث افزایش تقاضا برای دارایی‌های امن مانند طلا می‌شود.",
        "impact": {
            "طلا": "صعودی",
            "یورو": "خنثی",
            "بیت‌کوین": "تقویت",
            "نفت": "صعودی",
            "نقره": "تقویت"
        }
    }
]

# انتخاب یکی از خبرها به‌صورت تصادفی
news = sample_news[datetime.datetime.now().minute % len(sample_news)]

# ساخت پیام نهایی
message = f"📢 [خبر اقتصادی جدید]\n" \
          f"عنوان: {news['title']}\n" \
          f"تحلیل: {news['analysis']}\n" \
          f"تأثیر:\n" + "\n".join([f"- {k}: {v}" for k, v in news['impact'].items()])

# ارسال پیام به تلگرام
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "message_thread_id": THREAD_ID,
    "text": message
}

response = requests.post(url, data=payload)
print(response.text)
