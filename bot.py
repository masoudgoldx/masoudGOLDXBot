from news_engine import get_and_analyze_news
from tech_analysis import get_technical_analysis

# جمع‌آوری تحلیل فاندامنتال
fundamental = get_and_analyze_news()

# جمع‌آوری تحلیل تکنیکال
technical = get_technical_analysis()

# ترکیب پیام نهایی
msg = f"""📡 تحلیل لحظه‌ای بازار جهانی

📊 تحلیل فاندامنتال:
{fundamental}

📉 تحلیل تکنیکال:
{technical}
"""

# ارسال پیام به تلگرام
import requests
import os

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
requests.post(url, data={"chat_id": CHAT_ID, "text": msg})
