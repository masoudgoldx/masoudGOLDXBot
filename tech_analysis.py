def get_technical_analysis():
    try:
        btc = get_price("bitcoin")
        xau = get_price("tether-gold")
        eur = get_price("euro")

        analysis = f"""
        🔥 قیمت انس طلا: {xau} $
        🇺🇸 قیمت یورو: {eur} $
        ₿ قیمت بیت‌کوین: {btc} $

        ▼ تحلیل تکنیکال:
        انس: مقاومت در 2450 - حمایت در 2350
        یورو: نوسان محدود در محدوده 1.08-1.10
        بیت‌کوین: رنج بین 68 تا 72 هزار
        """
        return analysis

    except Exception as e:
        return f"خطا در تحلیل تکنیکال: {e}"
