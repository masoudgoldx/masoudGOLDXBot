import requests
from bs4 import BeautifulSoup

def get_technical_summary_investing(url):
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(res.text, "html.parser")
    try:
        signal = soup.select_one('.summaryTableWrapper .summary').text.strip()
        support = soup.select_one('.supportResistanceTable tbody tr:nth-child(1) td:nth-child(2)').text
        resistance = soup.select_one('.supportResistanceTable tbody tr:nth-child(2) td:nth-child(2)').text
    except:
        signal, support, resistance = "نامشخص", "?", "?"
    return signal, support, resistance

def main():
    # انس جهانی
    url_gold = "https://www.investing.com/commodities/gold-technical"
    sig_gold, sup_gold, res_gold = get_technical_summary_investing(url_gold)
    # یورو/دلار
    url_eur = "https://www.investing.com/currencies/eur-usd-technical"
    sig_eur, sup_eur, res_eur = get_technical_summary_investing(url_eur)
    # بیت‌کوین
    url_btc = "https://www.investing.com/crypto/bitcoin/btc-usd-technical"
    sig_btc, sup_btc, res_btc = get_technical_summary_investing(url_btc)

    msg = f"""[تحلیل تکنیکال خودکار امروز]

نماد: XAUUSD (انس جهانی)
سیگنال امروز: {sig_gold}
حمایت: {sup_gold} | مقاومت: {res_gold}

نماد: EURUSD
سیگنال امروز: {sig_eur}
حمایت: {sup_eur} | مقاومت: {res_eur}

نماد: BTCUSD
سیگنال امروز: {sig_btc}
حمایت: {sup_btc} | مقاومت: {res_btc}
"""

    url = f"https://api.telegram.org/bot7352244492:AAGOrkQXT88z1OH975q09jWkBcoI3G3ifEQ/sendMessage"
    payload = {
        "chat_id": "-1002586854094",
        "message_thread_id": 2,
        "text": msg
    }
    requests.post(url, data=payload)

if __name__ == "__main__":
    main()
