def build_message(title, data_list):
    """
    ساخت پیام نهایی برای ارسال به تلگرام
    """
    header = f"<b>{title}</b>\n"
    body = ""
    for item in data_list:
        body += f"{item}\n"
    return header + body
