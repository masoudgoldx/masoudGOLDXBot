def get_technical_analysis():
    real_prices = {
        "XAUUSD": 2384.50,
        "EURUSD": 1.0867,
        "BTCUSD": 67890.12
    }

    signals = {
        "XAUUSD": "خرید",
        "EURUSD": "فروش",
        "BTCUSD": "خنثی"
    }

    supports = {
        "XAUUSD": 2365.00,
        "EURUSD": 1.0800,
        "BTCUSD": 66000.00
    }

    resistances = {
        "XAUUSD": 2400.00,
        "EURUSD": 1.0900,
        "BTCUSD": 69000.00
    }

    report_lines = ["تحلیل تکنیکال خودکار:"]
    for symbol in real_prices:
        line = (
            f"{symbol}:\n"
            f" - قیمت: {real_prices[symbol]}\n"
            f" - سیگنال: {signals[symbol]}\n"
            f" - حمایت: {supports[symbol]}\n"
            f" - مقاومت: {resistances[symbol]}"
        )
        report_lines.append(line)

    return "\n\n".join(report_lines)
