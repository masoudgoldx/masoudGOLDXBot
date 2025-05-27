from telegram_sender import send_message
import requests
from datetime import datetime

def fetch_price(symbol):
    url = f"https://masoudgoldx.ir/bot/price_api.php?symbol={symbol}"
    r = requests.get(url)
    return r.json().get("price", "نامشخص")

def get_analysis(symbol):
    price = fetch_price(symbol)
    if symbol == "XAUUSD":
        return price, "2332", "2360", "📉 فشار فروش"
    elif symbol == "EURUSD":
        return price, "1.0800", "1.0900", "📈 صعود"
    elif symbol == "BTCUSD":
        return price, "65000", "68800", "⚠️ نوسان"

def format_technical(symbol):
    price, support, resistance, signal = get_analysis(symbol)
    today = datetime.now().strftime("%Y/%m/%d")
    return f"""📊 تحلیل {symbol}
قیمت: {price}
حمایت: {support}
مقاومت: {resistance}
سیگنال: {signal}
📅 {today}\n━━━━━━━━━━━━━━━"""

if __name__ == "__main__":
    for sym in ["XAUUSD", "EURUSD", "BTCUSD"]:
        send_message(format_technical(sym))
