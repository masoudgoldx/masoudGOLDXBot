import requests
import feedparser

BOT_TOKEN = "7352244492:AAGOrkQXT88z1OH975q09jWkBcoI3G3ifEQ"
CHAT_ID = "-1002586854094"
THREAD_ID = 2

SOURCES = [
    ("Investing", "https://www.investing.com/rss/news_25.rss"),
    ("Forexfactory", "https://www.forexfactory.com/ffcal_week_this.xml"),
    ("Coindesk", "https://coindesk.com/arc/outboundfeeds/rss/"),
    ("ایرنا", "https://www.irna.ir/rss.aspx"),
    ("تسنیم سیاسی", "https://www.tasnimnews.com/fa/rss/feed/1/%D8%A7%D8%AE%D8%A8%D8%A7%D8%B1-%D8%B3%DB%8C%D8%A7%D8%B3%DB%8C")
]

def translate_to_fa(text):
    try:
        url = "https://api.mymemory.translated.net/get"
        params = {"q": text, "langpair": "en|fa"}
        res = requests.get(url, params=params, timeout=10)
        data = res.json()
        return data["responseData"]["translatedText"]
    except:
        return text

def analyze(text):
    # کلمات کلیدی تحلیل جهانی/سیاسی
    pos = [
        "growth", "increase", "surge", "record high", "jump", "rise", "positive", 
        "توافق", "لغو تحریم", "برجام", "آتش‌بس", "صلح", "پیشرفت مذاکرات", "گشایش"
    ]
    neg = [
        "drop", "fall", "decline", "loss", "lower", "decrease", "down", "negative", 
        "تحریم", "شکست مذاکرات", "تحریم جدید", "تنش", "جنگ", "حمله", "درگیری", "اعتراض", "کاهش صادرات نفت", "افزایش تعرفه"
    ]
    region_pos = [
        "توافق", "لغو تحریم", "صادرات نفت", "آزادسازی پول‌های بلوکه شده", 
        "رشد صادرات", "پیشرفت مذاکرات", "گشایش", "امضای توافق"
    ]
    region_neg = [
        "تحریم", "شکست مذاکرات", "تعلیق صادرات", "قطع ارتباط", 
        "افزایش تحریم", "ممنوعیت صادرات", "تشدید تنش", "حمله"
    ]
    text_l = text.lower()
    # الگوریتم تحلیل ترکیبی اخبار اقتصادی و سیاسی
    if any(word in text_l for word in pos):
        ons = "مثبت (احتمال رشد)"
        gold = "مثبت (با تاخیر یا کمتر از انس)"
        dollar = "احتمال کاهش یا ثبات"
        eur = "مثبت"
        btc = "مثبت"
    elif any(word in text_l for word in neg):
        ons = "منفی (احتمال ریزش)"
        gold = "منفی (با تاخیر یا کمتر از انس)"
        dollar = "احتمال افزایش"
        eur = "منفی"
        btc = "منفی"
    elif any(word in text_l for word in region_pos):
        ons = "خنثی یا منفی (آرامش منطقه‌ای)"
        gold = "منفی (کاهش قیمت دلار و طلا داخلی)"
        dollar = "احتمال کاهش"
        eur = "خنثی"
        btc = "خنثی"
    elif any(word in text_l for word in region_neg):
        ons = "خنثی یا مثبت (تنش منطقه‌ای)"
        gold = "مثبت (افزایش قیمت دلار و طلا داخلی)"
        dollar = "احتمال افزایش"
        eur = "خنثی"
        btc = "خنثی"
    else:
        ons = "خنثی"
        gold = "خنثی"
        dollar = "خنثی"
        eur = "خنثی"
        btc = "خنثی"
    return ons, gold, dollar, eur, btc

def get_latest_news():
    news = []
    for name, url in SOURCES:
        try:
            feed = feedparser.parse(url)
            entry = feed.entries[0]
            title = entry.title
            summary = entry.summary if hasattr(entry, 'summary') else ""
            # ترجمه فقط اگر انگلیسی بود
            if name not in ["Forexfactory", "ایرنا", "تسنیم سیاسی"]:
                fa_title = translate_to_fa(title)
                fa_summary = translate_to_fa(summary)
            else:
                fa_title = title
                fa_summary = summary
            ons, gold, dollar, eur, btc = analyze(title + " " + summary)
            msg = f"""[خبر اقتصادی یا سیاسی جدید از {name}]
عنوان: {fa_title}
تحلیل: {fa_summary}
تأثیر:
- انس جهانی: {ons}
- طلای داخلی: {gold}
- دلار آزاد: {dollar}
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
