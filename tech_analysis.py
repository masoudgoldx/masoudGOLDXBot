import requests

def get_price(symbol):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
    response = requests.get(url, timeout=10)
    data = response.json()
    return data[symbol]["usd"]

def get_technical_analysis():
    try:
        btc = get_price("bitcoin")
        xau = get_price("tether-gold")
        eur = get_price("euro")

        analysis = f"""
        🔥 قیمت انس طلا: {xau} $
        🇺🇸 قیمت یورو (نماد دلار داخلی): {eur} $
        ₿ قیمت بیت‌کوین: {btc} $

        ▼ تحلیل تکنیکال:
        انس: مقاومت در 2450 - حمایت در 2350
        دلار: وابسته به نوسانات یورو و انس
        بیت‌کوین: وضعیت ناپایدار بین 68 تا 72 هزار
        """

        return analysis

    except Exception as e:
        return f"خطا در تحلیل تکنیکال: {e}"
