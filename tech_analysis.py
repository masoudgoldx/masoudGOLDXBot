import random

def analyze_symbol(symbol):
    signal = random.choice(["خرید", "فروش", "خنثی"])
    support = round(random.uniform(1900, 2000), 2)
    resistance = round(support + random.uniform(10, 50), 2)
    return {
        "نماد": symbol,
        "سیگنال": signal,
        "حمایت": support,
        "مقاومت": resistance,
    }

def get_technical_analysis():
    symbols = ["XAUUSD", "EURUSD", "BTCUSD"]
    report = "تحلیل تکنیکال روز:
"
    for symbol in symbols:
        result = analyze_symbol(symbol)
        report += (
            f"{result['نماد']}: سیگنال {result['سیگنال']} | حمایت {result['حمایت']} | مقاومت {result['مقاومت']}
"
        )
    return report