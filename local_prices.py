import requests
from bs4 import BeautifulSoup

def get_local_market():
    try:
        url = "https://www.tgju.org/"
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        def get_price_by_id(element_id):
            tag = soup.find("td", id=element_id)
            if tag:
                return tag.text.strip()
            else:
                return f"(یافت نشد: {element_id})"

        prices = {
            "دلار آزاد": get_price_by_id("price_dollar_rl"),
            "سکه امامی": get_price_by_id("price_sekee"),
            "طلا 18 عیار": get_price_by_id("price_geram18"),
            "انس جهانی": get_price_by_id("gold")
        }

        message = "\n".join([f"{key}: {value} تومان" for key, value in prices.items()])
        return f"قیمت‌های لحظه‌ای بازار:\n\n{message}"

    except Exception as e:
        return f"خطا در دریافت نرخ‌های بازار داخلی: {e}"
