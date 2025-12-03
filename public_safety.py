import random

class PublicPlaceSafetyAgent:
    def __init__(self, memory):
        self.memory = memory

    def analyze_frame(self, frame_id):
        threat = random.choice([True, False])
        if threat:
            self.memory.log_incident({
                "type": "public_safety_threat",
                "frame": frame_id
            })
        return threat
