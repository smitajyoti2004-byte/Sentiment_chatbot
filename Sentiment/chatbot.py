class ChatBot:
    def __init__(self, analyzer):
        self.analyzer = analyzer
        self.history = []

    def add_user_message(self, msg: str):
        self.history.append(msg)

    def reply(self, text: str) -> str:
        t = text.lower()

        if "hello" in t or "hi" in t:
            return "Hello! How can I assist you today?"

        if "sad" in t or "upset" in t:
            return "I’m sorry you’re feeling this way. Want to talk about it?"

        if "happy" in t or "good" in t:
            return "That's wonderful! What made you feel that way?"

        return "I understand. Tell me more."
