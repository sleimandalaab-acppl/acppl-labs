def analyze(self):
    results = []

    # 1. تجميع الأحداث
    failed_logins = sum(1 for e in self.events if e.name == "failed_logins")
    unusual_ips = sum(1 for e in self.events if e.name == "unusual_ips")

    # 2. تحليل سببي بسيط
    if failed_logins >= 3:
        results.append({
            "risk": "brute_force",
            "probability": 0.7,
            "cause": "multiple failed logins",
            "explanation": f"{failed_logins} failed login attempts detected"
        })

    if failed_logins >= 3 and unusual_ips >= 2:
        results.append({
            "risk": "credential_stuffing",
            "probability": 0.9,
            "cause": "failed logins + unusual IPs",
            "explanation": f"{failed_logins} failed logins from {unusual_ips} unusual IPs"
        })

    return results
