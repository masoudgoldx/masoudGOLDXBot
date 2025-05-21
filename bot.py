import os
from news_engine import get_and_analyze_news
from tech_analysis import get_technical_analysis
import requests

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
API_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

fundamental = get_and_analyze_news()
technical = get_technical_analysis()

# Ensure message is formatted correctly
msg = "\n".join(fundamental).strip() if fundamental else "هیچ خبر فاندامنتال جدیدی در دسترس نیست."
msg += "\n\n" + technical

params = {
    "chat_id": CHAT_ID,
    "text": msg
}

try:
    response = requests.post(API_URL, params=params)
    response.raise_for_status()
except Exception as e:
    print("Failed to send message:", e)
