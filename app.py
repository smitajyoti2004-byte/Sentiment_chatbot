import streamlit as st
from bot.analyzer import SentimentAnalyzer
from Sentiment.chatbot import ChatBot
from bot.storage import ChatStorage


st.set_page_config(page_title="Sentiment Chatbot", page_icon="🤖", layout="wide")

if "history" not in st.session_state:
    st.session_state.history = []

if "full_conversation" not in st.session_state:
    st.session_state.full_conversation = []

analyzer = SentimentAnalyzer()
bot = ChatBot(analyzer)
storage = ChatStorage()  # JSON storage handler

with st.sidebar:
    st.title("About Chatbot")
    st.write("This chatbot maintains full conversation history and performs sentiment analysis.")
    st.write("Type **end** to finish and see the final sentiment report.")
    st.divider()
    st.subheader("Example Prompts")
    st.write("- I feel happy today")
    st.write("- I am sad")
    st.write("- Hello chatbot")

# Main Chat Header
st.title("Sentiment Chatbot")
st.write("Chat with the bot and see sentiment analysis in real-time.")

# Display previous messages
for role, content in st.session_state.history:
    if role == "user":
        st.chat_message("user").write(content)
    else:
        st.chat_message("assistant").write(content)

# Chat input
user_input = st.chat_input("Type your message...")

if user_input:
    # Save user message
    st.session_state.history.append(("user", user_input))
    st.session_state.full_conversation.append(user_input)
    storage.save_message("user", user_input)

    # End conversation → final sentiment
    if user_input.lower() == "end":
        final_sentiment = analyzer.overall_sentiment(st.session_state.full_conversation)
        final_msg = f"Final Conversation Sentiment: **{final_sentiment}**"

        st.session_state.history.append(("assistant", final_msg))

        # Save final sentiment in JSON
        storage.save_final_sentiment(final_sentiment)

    else:
        # Tier 2: per-message sentiment
        sentiment = analyzer.get_sentiment(user_input)
        sentiment_msg = f"Sentiment: {sentiment}"

        st.session_state.history.append(("assistant", sentiment_msg))
        storage.save_message("assistant", sentiment_msg, sentiment)

        # Bot reply
        reply = bot.reply(user_input)
        st.session_state.history.append(("assistant", reply))
        storage.save_message("assistant", reply)

    st.rerun()
