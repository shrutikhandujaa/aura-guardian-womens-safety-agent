import datetime

class MemoryBank:
    def __init__(self):
        self.incidents = []

    def log_incident(self, incident):
        incident["timestamp"] = datetime.datetime.now().isoformat()
        self.incidents.append(incident)
        print("INCIDENT:", incident)

    def save_csv(self, path):
        import csv
        if not self.incidents:
            return
        keys = self.incidents[0].keys()
        with open(path, "w", newline="") as f:
            writer = csv.DictWriter(f, keys)
            writer.writeheader()
            writer.writerows(self.incidents)
