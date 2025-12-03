import json
import os
from datetime import datetime

class ChatStorage:
    def __init__(self, filename="chat_history.json"):
        self.filename = filename

        # Create JSON file if missing
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump({"conversations": [], "final_sentiment": None}, f, indent=4)

    def _load(self):
        with open(self.filename, "r") as f:
            return json.load(f)

    def _write(self, data):
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def save_message(self, role, message, sentiment=None):
        data = self._load()

        entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "role": role,
            "message": message,
            "sentiment": sentiment
        }

        data["conversations"].append(entry)
        self._write(data)

    def save_final_sentiment(self, sentiment):
        data = self._load()
        data["final_sentiment"] = sentiment
        self._write(data)
