from .memory import MemoryBank
from .shadow_walker import ShadowWalkerAgent
from .harassment_detector import HarassmentDetectorAgent
from .public_safety import PublicPlaceSafetyAgent

class GuardianAI:
    def __init__(self):
        self.memory = MemoryBank()
        self.shadow = ShadowWalkerAgent(self.memory)
        self.harassment = HarassmentDetectorAgent(self.memory)
        self.safety = PublicPlaceSafetyAgent(self.memory)
        self.paths = {}

    def feed_gps(self, user_id, location):
        if user_id not in self.paths:
            self.paths[user_id] = []
        self.paths[user_id].append(location)
        self.shadow.update(user_id, location)

    def feed_text(self, text):
        return self.harassment.detect_from_text(text)

    def feed_frame(self, frame_id):
        return self.safety.analyze_frame(frame_id)

    def check_following(self, user_id):
        return self.shadow.detect_following(user_id, self.paths)

    def save_memory(self, path):
        self.memory.save_csv(path)
