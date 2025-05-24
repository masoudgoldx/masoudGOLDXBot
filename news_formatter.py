
def format_news_item(title_en, summary_en, source, link):
    title_fa = translate_title(title_en)
    summary_fa = summarize(summary_en)
    effects = analyze_effect(title_en + " " + summary_en)

    message = f"""📢 {title_fa}

خلاصه خبر ✅
{summary_fa}

📊 تأثیرات احتمالی:
{effects}

منبع: {source}
{link}

تحلیل و گردآوری: Masoudgoldx
"""
    return message

def translate_title(title):
    if "inflation" in title.lower():
        return "📉 تورم در آمریکا رو به کاهش!"
    elif "gold" in title.lower():
        return "🏆 طلا در کانون توجه!"
    elif "interest rate" in title.lower():
        return "📌 نرخ بهره تحت تأثیر قرار گرفت"
    else:
        return "📢 خبر جدید اقتصادی"

def summarize(summary):
    if "inflation" in summary.lower():
        return "تورم سالانه در آمریکا کاهش یافت و کمتر از حد انتظار بود."
    elif "gold" in summary.lower():
        return "قانون جدیدی طلا را برای بانک‌ها ارزشمندتر می‌کند."
    else:
        return "خلاصه‌ای از خبر اقتصادی منتشر شده."

def analyze_effect(text):
    impact = ""
    text = text.lower()

    if "inflation" in text or "cpi" in text:
        impact += "📈 سهام: احتمال رشد\n"
        impact += "📉 دلار: احتمال تضعیف\n"
        impact += "🏅 طلا: احتمال افزایش قیمت"
    elif "gold" in text:
        impact += "📉 دلار: احتمال افت\n"
        impact += "🏅 طلا: احتمال رشد\n"
        impact += "📈 بازارهای جهانی: تحت تأثیر مثبت"
    else:
        impact += "⏳ نیاز به تحلیل بیشتر..."

    return impact
