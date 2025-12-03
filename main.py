# filepath: main.py
from bot.analyzer import SentimentAnalyzer
from Sentiment.chatbot import ChatBot


def main():
    analyzer = SentimentAnalyzer()
    bot = ChatBot(analyzer)

    print("Chatbot running. Type 'exit' to finish.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        bot.add_user_message(user_input)

        sentiment = analyzer.get_sentiment(user_input)
        print(f"→ Sentiment: {sentiment}")

        reply = bot.generate_reply(user_input)
        bot.add_bot_message(reply)
        print("Bot:", reply)

    print("\n--- FINAL SENTIMENT REPORT ---")
    user_messages = bot.get_user_messages_only()
    overall = analyzer.get_conversation_sentiment(user_messages)
    print("Overall conversation sentiment:", overall)


if __name__ == "__main__":
    main()
