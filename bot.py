
from news_engine import get_and_analyze_news
from tech_analysis import get_technical_analysis
from utils import send_telegram_message, load_last_message, save_last_message

def main():
    news_text = get_and_analyze_news()
    tech_text = get_technical_analysis()
    final_message = news_text + "\n\n" + tech_text

    if final_message.strip() != load_last_message():
        send_telegram_message(final_message)
        save_last_message(final_message)

if __name__ == "__main__":
    main()
