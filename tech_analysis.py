import random

def analyze_symbol(symbol):
    signal = random.choice(["صعودی", "نزولی", "خنثی"])
    support = round(random.uniform(1000, 2000), 2)
    resistance = round(random.uniform(2000, 3000), 2)

    return {
        "نماد": symbol,
        "سیگنال": signal,
        "حمایت": support,
        "مقاومت": resistance
    }

def get_technical_analysis():
    symbols = ["XAUUSD", "EURUSD", "BTCUSD"]
    report = "تحلیل تکنیکال خودکار امروز:\n"
    for symbol in symbols:
        result = analyze_symbol(symbol)
        report += (
            f"\nنماد: {result['نماد']}\n"
            f"سیگنال: {result['سیگنال']}\n"
            f"حمایت: {result['حمایت']}\n"
            f"مقاومت: {result['مقاومت']}\n"
        )
    return report
