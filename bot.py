
import os
import requests
from news_engine import get_and_analyze_news
from tech_analysis import get_technical_analysis
from local_prices import get_local_market
from economic_calendar import get_economic_calendar
from categorize_news import categorize_news_item

def send_telegram_message(message):
    token = os.getenv("BOT_TOKEN")
    chat_id = os.getenv("CHAT_ID")

    if not token or not chat_id:
        print("[Error] BOT_TOKEN or CHAT_ID is not set!")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    max_length = 4000
    parts = [message[i:i+max_length] for i in range(0, len(message), max_length)]

    for idx, part in enumerate(parts):
        data = {
            "chat_id": chat_id,
            "text": part
        }
        response = requests.post(url, data=data)
        print(f"[Telegram] Part {idx+1}/{len(parts)} Status: {response.status_code}")
        print(f"[Telegram] Part {idx+1} Response: {response.text}")

if __name__ == "__main__":
    fundamental = get_and_analyze_news()
    technical = get_technical_analysis()
    local = get_local_market()
    calendar = get_economic_calendar()

    categorized = {'انس طلا': [], 'یورو': [], 'بیت‌کوین': [], 'متفرقه': []}
    for item in fundamental:
        cat = categorize_news_item(item)
        categorized[cat].append(item)

    fundamental_message = """اخبار فاندامنتال دسته‌بندی‌شده:

"""
    for key, items in categorized.items():
        if items:
            fundamental_message += f"== {key} ==\n"
            for i in items:
                fundamental_message += f"{i['title']}\n{i['summary']}\n{i['link']}\n\n"

    message = fundamental_message + "\n\n" + technical + "\n\n" + local + "\n\n" + calendar
    send_telegram_message(message)
