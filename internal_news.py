import feedparser
from bs4 import BeautifulSoup

sources = [
    ("https://www.irna.ir/rss", "IRNA"),
    ("https://www.mehrnews.com/rss", "MEHR"),
    ("https://www.farsnews.ir/rss", "FARS")
]

keywords_dollar_up = ["تحریم", "نرخ ارز", "کاهش عرضه", "ناترازی", "افزایش تقاضا"]
keywords_dollar_down = ["توافق", "برجام", "عرضه ارز", "کنترل نرخ", "مداخله"]

def analyze_internal_sentiment(text):
    score = 0
    for word in keywords_dollar_up:
        if word in text:
            score += 1
    for word in keywords_dollar_down:
        if word in text:
            score -= 1
    if score > 0:
        return "احتمال افزایش دلار/طلا داخلی"
    elif score < 0:
        return "احتمال کاهش دلار/طلا داخلی"
    else:
        return "اثر خاصی مشاهده نشد"

def get_internal_news():
    results = []
    for url, source in sources:
        feed = feedparser.parse(url)
        for entry in feed.entries[:2]:
            title = BeautifulSoup(entry.title, "html.parser").text
            summary = BeautifulSoup(entry.get("summary", ""), "html.parser").text
            content = title + " " + summary
            sentiment = analyze_internal_sentiment(content)
            results.append(f"[{source}]
{title}
تحلیل اثر: {sentiment}")
    return "\n\n".join(results)