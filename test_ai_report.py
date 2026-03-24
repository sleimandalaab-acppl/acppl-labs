from acppl.ai_assistant import summarize_results

# أمثلة بيانات اختبار
results = [
    {"risk": "brute_force", "cause": "150 failed login attempts", "explanation": "Multiple failed logins"},
    {"risk": "weak_passwords", "cause": "simple passwords used", "explanation": "Many weak passwords"},
    {"risk": "unusual_ip", "cause": "login from unknown country", "explanation": "IP from new place"},
    {"risk": "data_leak", "cause": "api keys exposed online", "explanation": "Secrets found in repos"}
]

print(summarize_results(results))
