def generate_signal(price):
    if price < 2000:
        return "Buy", 1980, 2020
    elif price > 2100:
        return "Sell", 2080, 2120
    else:
        return "Neutral", 2000, 2100

def format_analysis(symbol, signal, support, resistance):
    return f"نماد: {symbol}
سیگنال امروز: {signal}
حمایت: {support} | مقاومت: {resistance}\n"

def run():
    analysis = "[تحلیل تکنیکال خودکار امروز]\n"
    for symbol, price in {"XAUUSD": 2045, "EURUSD": 1.085, "BTCUSD": 67200}.items():
        signal, support, resistance = generate_signal(price)
        analysis += format_analysis(symbol, signal, support, resistance)
    return analysis

if __name__ == "__main__":
    import requests
    message = run()
    url = "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/sendMessage"
    payload = {
        "chat_id": "<YOUR_CHAT_ID>",
        "message_thread_id": 2,
        "text": message
    }
    requests.post(url, data=payload)
