class HarassmentDetectorAgent:
    def __init__(self, memory):
        self.memory = memory
        self.keywords = ["stop", "help", "follow", "leave me"]

    def detect_from_text(self, text):
        t = text.lower()
        for word in self.keywords:
            if word in t:
                self.memory.log_incident({
                    "type": "harassment",
                    "text": text,
                    "keyword": word
                })
                return True
        return False
