from news_engine import get_and_analyze_news
from tech_analysis import get_technical_analysis

fundamental = get_and_analyze_news()
technical = get_technical_analysis()

msg = f"""📡 تحلیل لحظه‌ای بازار جهانی

📊 تحلیل فاندامنتال:
{fundamental if fundamental.strip() else 'هیچ خبر فاندامنتال جدیدی در دسترس نیست.'}

📉 تحلیل تکنیکال:
{technical}
"""

# ارسال پیام به تلگرام حتی اگر تحلیل فاندامنتال خالی باشد
import requests
import os

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
requests.post(url, data={"chat_id": CHAT_ID, "text": msg})
