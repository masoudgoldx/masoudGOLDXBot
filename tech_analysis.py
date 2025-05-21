import requests

def send_telegram_message(message):
    url = "https://api.telegram.org/bot7352244492:AAGOrkQXT88z1OH975q09jWkBcoI3G3ifEQ/sendMessage"
    payload = {
        "chat_id": "-1002586854094",
        "message_thread_id": 2,
        "text": message
    }
    requests.post(url, data=payload)

def get_technical(symbol):
    try:
        url = f"https://www.tradingview.com/symbols/{symbol}/technicals/"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        if response.ok and "summary" in response.text:
            # تحلیل دستی چون API رسمی نداره
            return f"سیگنال امروز {symbol}: نامشخص\nحمایت: ؟ | مقاومت: ؟"
        else:
            return f"سیگنال امروز {symbol}: نامشخص\nحمایت: ؟ | مقاومت: ؟"
    except:
        return f"سیگنال امروز {symbol}: نامشخص\nحمایت: ؟ | مقاومت: ؟"

if __name__ == "__main__":
    result = "تحلیل تکنیکال خودکار امروز\n\n"
    result += "نماد: XAUUSD (انس جهانی)\n" + get_technical("XAUUSD") + "\n\n"
    result += "نماد: EURUSD\n" + get_technical("EURUSD") + "\n\n"
    result += "نماد: BTCUSD\n" + get_technical("BTCUSD")
    send_telegram_message(result)
