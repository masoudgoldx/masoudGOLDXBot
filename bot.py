import os
import requests
from news_engine import get_and_analyze_news
from tech_analysis import get_technical_analysis

news_report = get_and_analyze_news()
technical_report = get_technical_analysis()

msg = (
    "تحلیل فاندامنتال:
"
    + news_report
    + "
-----------------------------
"
    + "تحلیل تکنیکال:
"
    + technical_report
)

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": msg,
}

response = requests.post(url, data=payload)
print("Message sent:", response.status_code == 200)