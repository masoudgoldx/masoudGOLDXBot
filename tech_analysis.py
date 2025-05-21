import requests
from bs4 import BeautifulSoup

def get_signals(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    table = soup.find('table', class_='technicalSummaryTbl')
    if not table:
        print("❌ جدول تکنیکال پیدا نشد! شاید Investing اجازه دسترسی نمی‌دهد یا آی‌پی محدود شده.")
        return "نامشخص", "?", "?"

    rows = table.find_all('tr')
    print(f"✅ تعداد ردیف جدول: {len(rows)}")
    for i, row in enumerate(rows):
        print(f"ردیف {i}: {row.text}")

    # حالا بررسی می‌کنیم ردیف مناسب وجود دارد یا نه
    if len(rows) > 2:
        tds = rows[2].find_all('td')
        print("🟢 سلول‌های ردیف سوم:", [td.text for td in tds])
        try:
            signal = tds[1].text.strip()
            support = tds[4].text.strip()
            resistance = tds[5].text.strip()
        except Exception as e:
            print("خطا در استخراج مقادیر:", e)
            signal = "نامشخص"
            support = "?"
            resistance = "?"
    else:
        print("❗️ ردیف کافی برای استخراج سیگنال وجود ندارد.")
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

# اگر فقط لاگ و تست می‌خواهی خط پایین را فعال نکن.
# اگر می‌خواهی پیام به تلگرام بفرستی، این بخش را فعال کن و توکن و آیدی را بذار:
'''
BOT_TOKEN = "توکن_بات"
CHAT_ID = "-1002586854094"
THREAD_ID = 2

telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "message_thread_id": THREAD_ID,
    "text": msg
}
requests.post(telegram_url, data=payload)
'''
