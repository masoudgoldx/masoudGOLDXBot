import requests

signals = {
    "XAUUSD": {"signal": "خنثی", "support": "2285", "resistance": "2370"},
    "EURUSD": {"signal": "صعودی", "support": "1.0800", "resistance": "1.0970"},
    "BTCUSD": {"signal": "نزولی", "support": "66000", "resistance": "70000"},
}

def send_telegram_message(message):
    url = "https://api.telegram.org/bot7352244492:AAGOrkQXT88z1OH975q09jWkBcoI3G3ifEQ/sendMessage"
    payload = {
        "chat_id": "-1002586854094",
        "message_thread_id": 2,
        "text": message
    }
    requests.post(url, data=payload)

def build_analysis():
    text = "【تحلیل تکنیکال خودکار امروز】\n"
    for symbol, data in signals.items():
        text += f"نماد: {symbol}\nسیگنال امروز: {data['signal']}\nحمایت: {data['support']} | مقاومت: {data['resistance']}\n\n"
    return text

if __name__ == "__main__":
    msg = build_analysis()
    send_telegram_message(msg)
