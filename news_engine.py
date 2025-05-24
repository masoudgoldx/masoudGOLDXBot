import feedparser
from bs4 import BeautifulSoup

def get_and_analyze_news():
    feeds = [
        ("https://www.investing.com/rss/news_301.rss", "Investing"),
        ("https://feeds.bbci.co.uk/news/world/rss.xml", "BBC"),
        ("https://www.tabnak.ir/fa/rss/3/0", "Tabnak"),
    ]

    news_items = []
    for url, source in feeds:
        feed = feedparser.parse(url)
        for entry in feed.entries[:3]:
            title = entry.title
            summary = BeautifulSoup(entry.get("summary", ""), "html.parser").text.strip()
            link = entry.link
            news_items.append(f"• {title} ({source})
{summary}
{link}")

    return "

".join(news_items)