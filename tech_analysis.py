import requests
from bs4 import BeautifulSoup

def get_signals(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    try:
        table = soup.find('table', class_='technicalSummaryTbl')
        rows = table.find_all('tr')
        # روند اصلی روزانه
        signal = rows[2].find_all('td')[1].text.strip()
        # حمایت و مقاومت
        support = rows[2].find_all('td')[4].text.strip()
        resistance = rows[2].find_all('td')[5].text.strip()
    except Exception:
        signal = "نامشخص"
        support = "?"
        resistance = "?"

    return signal, support, resistance

urls = {
    "XAUUSD": "https://www.investing.com/technical/technical-summary?pair=8830",
    "EURUSD": "https://www.investing.com/technical/technical-summary?pair=1",
    "BTCUSD": "https://www.investing.com/technical/technical-summary?pair=1057391"
}

signals = {}

for symbol, url in urls.items():
    signal, support, resistance = get_signals(url)
    signals[symbol] = {
        "signal": signal,
        "support": support,
        "resistance": resistance
    }

msg = (
    "[تحلیل تکنیکال خودکار امروز]\n"
    f"نماد: XAUUSD (انس جهانی)\n"
    f"سیگنال امروز: {signals['XAUUSD']['signal']}\n"
    f"حمایت: {signals['XAUUSD']['support']} | مقاومت: {signals['XAUUSD']['resistance']}\n\n"
    f"نماد: EURUSD\n"
    f"سیگنال امروز: {signals['EURUSD']['signal']}\n"
    f"حمایت: {signals['EURUSD']['support']} | مقاومت: {signals['EURUSD']['resistance']}\n\n"
    f"نماد: BTCUSD\n"
    f"سیگنال امروز: {signals['BTCUSD']['signal']}\n"
    f"حمایت: {signals['BTCUSD']['support']} | مقاومت: {signals['BTCUSD']['resistance']}\n"
)

# توکن و آیدی مخصوص MasoudGOLDXBot
BOT_TOKEN = "7352244492:AAGOrkQXT88z1OH975q09jWkBcoI3G3ifEQ"
CHAT_ID = "-1002586854094"
THREAD_ID = 2

telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "message_thread_id": THREAD_ID,
    "text": msg
}
requests.post(telegram_url, data=payload)
