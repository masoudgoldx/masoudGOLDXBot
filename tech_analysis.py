import requests

def get_price(symbol):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data[symbol]["usd"]

def get_technical_analysis():
    try:
        btc = get_price("bitcoin")
        xau = get_price("tether-gold")  # جایگزین انس طلا
        eur = get_price("euro")

        analysis = f"""
💰 قیمت انس طلا: {xau} $
💶 قیمت یورو: {eur} $
🟡 قیمت بیت‌کوین: {btc} $

🔻 وضعیت تکنیکال:
• انس: مقاومت در 2450 - حمایت در 2350
• یورو: روند صعودی با احتمال پولبک
• بیت‌کوین: نوسان شدید در محدوده 68K
"""
        return analysis
    except Exception as e:
        return "خطا در تحلیل تکنیکال"
