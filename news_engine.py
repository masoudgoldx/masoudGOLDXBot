
import feedparser

def fake_translate(text):
    # ترجمه ساده بدون نیاز به API
    replacements = {
        "gold": "طلا",
        "bitcoin": "بیت‌کوین",
        "euro": "یورو",
        "usd": "دلار",
        "interest rate": "نرخ بهره",
        "inflation": "تورم",
        "fed": "فدرال رزرو",
        "rises": "افزایش",
        "falls": "کاهش",
        "market": "بازار",
        "prices": "قیمت‌ها",
        "strong": "قوی",
        "weak": "ضعیف"
    }
    for eng, fa in replacements.items():
        text = text.replace(eng, fa).replace(eng.title(), fa)
    return text

def detect_asset_impact(text):
    text = text.lower()
    if any(word in text for word in ['gold', 'precious']):
        return 'انس طلا'
    elif any(word in text for word in ['euro', 'ecb']):
        return 'یورو'
    elif any(word in text for word in ['bitcoin', 'crypto', 'btc']):
        return 'بیت‌کوین'
    else:
        return 'متفرقه'

def get_and_analyze_news():
    url = "https://www.investing.com/rss/news_25.rss"
    feed = feedparser.parse(url)
    categorized = {'انس طلا': [], 'یورو': [], 'بیت‌کوین': [], 'متفرقه': []}

    for entry in feed.entries[:10]:
        title = fake_translate(entry.title)
        summary = fake_translate(entry.summary)
        impact = detect_asset_impact(entry.title + " " + entry.summary)
        effect = f"تأثیر احتمالی بر {impact.lower()}"

        categorized[impact].append({
            "title": title,
            "summary": summary,
            "impact": effect,
            "link": entry.link
        })

    return categorized
