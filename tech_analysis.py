import requests
from bs4 import BeautifulSoup

BOT_TOKEN = "توکن ربات"
CHAT_ID = "-1002586854094"
THREAD_ID = 2

def get_technical_signal(symbol):
    url = f"https://www.investing.com/currencies/{symbol}-technical"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "X-Requested-With": "XMLHttpRequest"
    }
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        signal = soup.select_one(".summaryTable tr:nth-child(1) td:nth-child(2)").text.strip()
        support = soup.select_one(".summaryTable tr:nth-child(3) td:nth-child(2)").text.strip()
        resistance = soup.select_one(".summaryTable tr:nth-child(4) td:nth-child(2)").text.strip()
        return signal, support, resistance
    except:
        return "نامشخص", "?", "?"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "message_thread_id": THREAD_ID,
        "text": message
    }
    requests.post(url, data=payload)

if __name__ == "__main__":
    # نمادهای مورد نظر
    pairs = {
        "xau-usd": "XAUUSD (انس جهانی)",
        "eur-usd": "EURUSD",
        "btc-usd": "BTCUSD"
    }

    msg = "[تحلیل تکنیکال خودکار امروز]\n"

    for symbol_url, symbol_name in pairs.items():
        signal, support, resistance = get_technical_signal(symbol_url)
        msg += (
            f"\nنماد: {symbol_name}\n"
            f"سیگنال: {signal}\n"
            f"حمایت: {support} | مقاومت: {resistance}\n"
        )

    send_telegram_message(msg)
