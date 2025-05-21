import requests

def get_technical_analysis():
    try:
        gold = requests.get("https://api.metals.live/v1/spot").json()[0]["gold"]
        btc = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd").json()["bitcoin"]["usd"]
        eurusd = requests.get("https://open.er-api.com/v6/latest/EUR").json()["rates"]["USD"]
    except:
        return "خطا در دریافت داده تکنیکال."

    return f"""
XAUUSD:
- قیمت: {gold}
- حمایت: {round(gold - 10, 2)}, مقاومت: {round(gold + 10, 2)}

EURUSD:
- قیمت: {eurusd}
- حمایت: {round(eurusd - 0.005, 4)}, مقاومت: {round(eurusd + 0.005, 4)}

BTCUSD:
- قیمت: {btc}
- حمایت: {round(btc - 1000)}, مقاومت: {round(btc + 1000)}
""".strip()