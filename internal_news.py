
import feedparser
from bs4 import BeautifulSoup

sources = [
    ("https://www.irna.ir/rss", "IRNA"),
    ("https://www.farsnews.ir/rss", "FARS"),
    ("https://www.mehrnews.com/rss", "MEHR")
]

keywords_dollar_up = ["تحریم", "نرخ ارز", "کاهش عرضه ارز", "ناترازی", "سیاست ارزی", "افزایش تقاضا"]
keywords_dollar_down = ["توافق", "برجام", "عرضه ارز", "کنترل نرخ", "ارزپاشی", "مداخله بانک مرکزی"]

def analyze_internal_sentiment(text):
    score = 0
    for word in keywords_dollar_up:
        if word in text:
            score += 1
    for word in keywords_dollar_down:
        if word in text:
            score -= 1
    if score > 0:
        return "احتمال افزایش نرخ دلار و طلا داخلی"
    elif score < 0:
        return "احتمال کاهش نرخ دلار و طلا داخلی"
    else:
        return "اثر خاصی مشاهده نشد"

def get_internal_news():
    results = []
    for url, source in sources:
        feed = feedparser.parse(url)
        for entry in feed.entries[:3]:
            title = BeautifulSoup(entry.title, "html.parser").text
            summary = BeautifulSoup(entry.get("summary", ""), "html.parser").text
            content = title + " " + summary
            sentiment = analyze_internal_sentiment(content)
            results.append(f"[{source}]\n{title}\nتحلیل اثر: {sentiment}\n")
    return "\n".join(results)
