
import feedparser
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

keywords_positive = {
    "طلا": ["افزایش تقاضا", "ریسک", "تورم", "بحران"],
    "دلار": ["افزایش نرخ بهره", "بازار کار قوی", "اقتصاد آمریکا"],
    "بیت‌کوین": ["پذیرش", "ETF", "سرمایه‌گذاری"]
}

keywords_negative = {
    "طلا": ["کاهش تقاضا", "آرامش بازار", "افزایش نرخ بهره آمریکا"],
    "دلار": ["رکود", "کاهش نرخ بهره", "بحران بانکی"],
    "بیت‌کوین": ["ممنوعیت", "هک", "ریزش"]
}

def get_news_sources():
    return [
        ("https://www.investing.com/rss/news_301.rss", "Investing"),
        ("https://feeds.feedburner.com/CoinDesk", "Coindesk")
    ]

def analyze_sentiment(text):
    result = {"طلا": 0, "دلار": 0, "بیت‌کوین": 0}
    for asset in result:
        for pos_kw in keywords_positive[asset]:
            if pos_kw in text:
                result[asset] += 1
        for neg_kw in keywords_negative[asset]:
            if neg_kw in text:
                result[asset] -= 1
    return result

def interpret_sentiment(sentiment):
    direction = {}
    for asset, score in sentiment.items():
        if score > 0:
            direction[asset] = "احتمال رشد"
        elif score < 0:
            direction[asset] = "احتمال افت"
        else:
            direction[asset] = "بدون تغییر مشخص"
    return direction

def get_and_analyze_news():
    all_news = []
    for url, source in get_news_sources():
        feed = feedparser.parse(url)
        for entry in feed.entries[:3]:
            title_en = entry.title
            try:
                title = GoogleTranslator(source='auto', target='fa').translate(title_en)
            except:
                title = title_en
            summary = BeautifulSoup(entry.summary, 'html.parser').text.strip() if hasattr(entry, "summary") else ""
            full_text = f"{title} - {summary}"
            sentiment = analyze_sentiment(full_text)
            directions = interpret_sentiment(sentiment)
            result = {
                "source": source,
                "title": title,
                "summary": summary,
                "directions": directions
            }
            all_news.append(result)
    return all_news
