
from news_engine import get_and_analyze_news
from tech_analysis import get_technical_analysis
from internal_news import get_internal_news
from utils import send_telegram_message, load_last_message, save_last_message

def main():
    internal = get_internal_news()
    international = get_and_analyze_news()
    technical = get_technical_analysis()

    final_message = (
        "اخبار داخلی و اثرگذاری بر بازار:"

" + internal + 
        "

--------------------------

" +
        "اخبار بین‌المللی مهم:

" + international +
        "

--------------------------

" +
        technical
    )

    if final_message.strip() != load_last_message():
        send_telegram_message(final_message)
        save_last_message(final_message)

if __name__ == "__main__":
    main()
