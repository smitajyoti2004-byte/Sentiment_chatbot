from textblob import TextBlob

class SentimentAnalyzer:
    def get_sentiment(self, text: str) -> str:
        polarity = TextBlob(text).sentiment.polarity

        if polarity > 0:
            return "Positive"
        if polarity < 0:
            return "Negative"
        return "Neutral"

    def overall_sentiment(self, messages: list[str]) -> str:
        combined = " ".join(messages)
        return self.get_sentiment(combined)
