class Event:
    def __init__(self, name, count=1):
        self.name = name
        self.count = count


class CausalEngine:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def analyze(self):
        results = []

        for event in self.events:
            if event.name == "failed_logins" and event.count > 100:
                results.append({
                    "risk": "brute_force",
                    "reason": "too many failed logins",
                    "action": "block_ip"
                })

        return results


# مثال بسيط للتجربة
if __name__ == "__main__":
    engine = CausalEngine()
    engine.add_event(Event("failed_logins", 150))

    results = engine.analyze()

    for r in results:
        print("Risk:", r["risk"])
        print("Reason:", r["reason"])
        print("Action:", r["action"])
