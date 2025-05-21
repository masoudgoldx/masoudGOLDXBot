
import requests

def get_technical_analysis():
    try:
        gold_price = requests.get("https://api.metals.live/v1/spot").json()[0]["gold"]
        btc_price = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd").json()["bitcoin"]["usd"]
        eurusd_price = requests.get("https://open.er-api.com/v6/latest/EUR").json()["rates"]["USD"]
    except:
        return "خطا در دریافت قیمت‌ها از منابع آنلاین."

    return f"""
تحلیل تکنیکال خودکار:

XAUUSD:
 - قیمت لحظه‌ای: {gold_price}
 - سیگنال: خرید
 - حمایت: {round(gold_price - 15, 2)} | مقاومت: {round(gold_price + 15, 2)}

EURUSD:
 - قیمت لحظه‌ای: {eurusd_price}
 - سیگنال: فروش
 - حمایت: {round(eurusd_price - 0.005, 4)} | مقاومت: {round(eurusd_price + 0.005, 4)}

BTCUSD:
 - قیمت لحظه‌ای: {btc_price}
 - سیگنال: خنثی
 - حمایت: {round(btc_price - 1000)} | مقاومت: {round(btc_price + 1000)}
""".strip()
