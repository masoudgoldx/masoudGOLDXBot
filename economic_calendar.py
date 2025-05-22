from datetime import datetime

def get_economic_calendar():
    today = datetime.now().strftime("%Y-%m-%d")

    events = [
        {"time": "09:00", "currency": "USD", "event": "Core CPI (MoM)", "impact": "High"},
        {"time": "11:30", "currency": "EUR", "event": "ECB President Speech", "impact": "Medium"},
        {"time": "15:00", "currency": "USD", "event": "FOMC Member Speech", "impact": "Low"},
    ]

    msg = f"تقویم اقتصادی امروز ({today}):\n\n"
    for e in events:
        msg += f"{e['time']} - {e['currency']} - {e['event']} [{e['impact']} Impact]\n"

    return msg
