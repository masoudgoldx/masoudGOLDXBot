
import random

def analyze_symbol(symbol):
    if symbol == "XAUUSD":
        support = round(random.uniform(2280, 2350), 2)
        resistance = round(support + random.uniform(10, 30), 2)
    elif symbol == "BTCUSD":
        support = round(random.uniform(60000, 68000), 0)
        resistance = round(support + random.uniform(1500, 3000), 0)
    elif symbol == "EURUSD":
        support = round(random.uniform(1.07, 1.09), 4)
        resistance = round(support + random.uniform(0.0030, 0.0080), 4)
    else:
        support = 0
        resistance = 0

    signal = random.choice(["خرید", "فروش", "نامشخص"])

    return {
        "نماد": symbol,
        "سیگنال": signal,
        "حمایت": support,
        "مقاومت": resistance
    }

def get_technical_analysis():
    symbols = ["XAUUSD", "EURUSD", "BTCUSD"]
    report = "تحلیل تکنیکال خودکار امروز:

"
    for symbol in symbols:
        result = analyze_symbol(symbol)
        report += (
            f"نماد: {result['نماد']}
"
            f"سیگنال امروز: {result['سیگنال']}
"
            f"حمایت: {result['حمایت']} | مقاومت: {result['مقاومت']}

"
        )
    return report.strip()
