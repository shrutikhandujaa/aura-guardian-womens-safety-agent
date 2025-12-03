class ShadowWalkerAgent:
    def __init__(self, memory):
        self.memory = memory
        self.tracks = {}

    def update(self, user_id, location):
        if user_id not in self.tracks:
            self.tracks[user_id] = []
        self.tracks[user_id].append(location)

    def detect_following(self, user_id, all_paths):
        user_path = self.tracks.get(user_id, [])
        if len(user_path) < 3:
            return False

        for other_id, path in all_paths.items():
            if other_id == user_id:
                continue
            if path[-1] == user_path[-1]:
                self.memory.log_incident({
                    "type": "following_detected",
                    "user": user_id,
                    "follower": other_id
                })
                return True

        return False
