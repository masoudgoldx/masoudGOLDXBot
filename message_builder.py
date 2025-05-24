
def build_message(news_by_asset, tech, local, calendar):
    message = "📢 گزارش روزانه Masoudgoldx\n\n"

    for asset, items in news_by_asset.items():
        if items:
            message += f"== {asset} ==\n"
            for item in items:
                message += f"{item['title']}\n{item['summary']}\n{item['impact']}\n{item['link']}\n\n"

    message += tech + "\n\n"
    message += local + "\n\n"
    message += calendar + "\n\n"
    message += "تحلیل و گردآوری: Masoudgoldx"
    return message
