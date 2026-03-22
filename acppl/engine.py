class CausalEngine:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def analyze(self):
        results = []

        for event in self.events:
            if event.name == "failed_logins":
                results.append({
                    "risk": "brute_force",
                    "probability": 0.85,
                    "reason": "عدد كبير من محاولات تسجيل الدخول الفاشلة"
                })

        return results
