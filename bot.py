import requests
import feedparser

# اطلاعات ربات
BOT_TOKEN = "7352244492:AAGOrkQXT88z1OH975q09jWkBcoI3G3ifEQ"
CHAT_ID = "-1002586854094"
THREAD_ID = 2

# منابع خبر
SOURCES = [
    ("Investing", "https://www.investing.com/rss/news_25.rss"),
    ("Forexfactory", "https://www.forexfactory.com/ffcal_week_this.xml"),
    ("Coindesk", "https://coindesk.com/arc/outboundfeeds/rss/")
]

def translate_to_fa(text):
    # ترجمه رایگان با MyMemory
    try:
        url = "https://api.mymemory.translated.net/get"
        params = {"q": text, "langpair": "en|fa"}
        res = requests.get(url, params=params, timeout=10)
        data = res.json()
        return data["responseData"]["translatedText"]
    except:
        return text

def analyze(text):
    pos = ["growth", "increase", "surge", "record high", "jump", "rise", "positive"]
    neg = ["drop", "fall", "decline", "loss", "lower", "decrease", "down", "negative"]
    text_l = text.lower()
    if any(word in text_l for word in pos):
        gold = "مثبت (احتمال رشد)"
        eur = "مثبت"
        btc = "مثبت"
    elif any(word in text_l for word in neg):
        gold = "منفی (احتمال ریزش)"
        eur = "منفی"
        btc = "منفی"
    else:
        gold = "خنثی"
        eur = "خنثی"
        btc = "خنثی"
    return gold, eur, btc

def get_latest_news():
    news = []
    for name, url in SOURCES:
        try:
            feed = feedparser.parse(url)
            entry = feed.entries[0]
            title = entry.title
            summary = entry.summary if hasattr(entry, 'summary') else ""
            # ترجمه فقط اگر انگلیسی بود
            if name != "Forexfactory":
                fa_title = translate_to_fa(title)
                fa_summary = translate_to_fa(summary)
            else:
                fa_title = title
                fa_summary = summary
            gold, eur, btc = analyze(title + " " + summary)
            msg = f"""[خبر اقتصادی جدید از {name}]
عنوان: {fa_title}
تحلیل: {fa_summary}
تأثیر:
- طلا: {gold}
- یورو: {eur}
- بیت‌کوین: {btc}
"""
            news.append(msg)
        except Exception as e:
            continue
    return news

def send_news(news_list):
    for msg in news_list:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "message_thread_id": THREAD_ID,
            "text": msg
        }
        requests.post(url, data=payload)

if __name__ == "__main__":
    news_list = get_latest_news()
    send_news(news_list)
