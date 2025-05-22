def categorize_news_item(item):
    title = item.get('title', '').lower()
    summary = item.get('summary', '').lower()

    if any(word in title for word in ['gold', 'metal', 'precious']) or 'gold' in summary:
        return 'انس طلا'
    elif any(word in title for word in ['euro', 'ecb', 'europe']):
        return 'یورو'
    elif any(word in title for word in ['bitcoin', 'crypto', 'btc']):
        return 'بیت‌کوین'
    else:
        return 'متفرقه'
