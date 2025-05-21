msg = (
    "[تحلیل تکنیکال خودکار امروز]\n"
    f"نماد: XAUUSD (انس جهانی)\n"
    f"سیگنال: {signals['XAUUSD']['signal']}\n"
    f"حمایت: {signals['XAUUSD']['support']} | مقاومت: {signals['XAUUSD']['resistance']}\n\n"
    f"نماد: EURUSD\n"
    f"سیگنال: {signals['EURUSD']['signal']}\n"
    f"حمایت: {signals['EURUSD']['support']} | مقاومت: {signals['EURUSD']['resistance']}\n\n"
    f"نماد: BTCUSD\n"
    f"سیگنال: {signals['BTCUSD']['signal']}\n"
    f"حمایت: {signals['BTCUSD']['support']} | مقاومت: {signals['BTCUSD']['resistance']}"
)

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "message_thread_id": THREAD_ID,
        "text": message
    }
    requests.post(url, data=payload)

if __name__ == "__main__":
    send_telegram_message(msg)
