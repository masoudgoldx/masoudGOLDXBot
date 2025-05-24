
from datetime import datetime

def get_economic_calendar():
    today = datetime.now().strftime("%Y-%m-%d")
    return f"""🗓️ تقویم اقتصادی امروز ({today}):
- 09:00 🇺🇸 Core CPI (اهمیت بالا)
- 11:30 🇪🇺 سخنرانی رئیس ECB (اهمیت متوسط)
- 15:00 🇺🇸 نشست FOMC (اهمیت بالا)"""
