# acppl/ai_assistant.py

def explain_risk(risk):
    """
    يحول خطر واحد إلى تقرير مفصل مع توصيات مخصصة حسب نوع الخطر.
    """
    risk_type = risk.get('risk', 'unknown').lower()
    cause = risk.get('cause', 'Unknown')
    explanation_text = risk.get('explanation', 'No further details')

    # نصائح افتراضية
    recommendations = ["Review system logs", "Investigate further"]

    # تخصيص التوصيات حسب نوع الخطر
    if risk_type == "brute_force":
        recommendations = ["Enable rate limiting", "Strengthen passwords", "Monitor unusual IPs"]
    elif risk_type == "weak_passwords":
        recommendations = ["Force password complexity", "Enable 2FA", "Monitor password changes"]
    elif risk_type == "unusual_ip":
        recommendations = ["Alert on new IPs", "Check geolocation", "Enable MFA for suspicious logins"]
    elif risk_type == "data_leak":
        recommendations = ["Rotate secrets", "Check for exposed credentials", "Enhance encryption"]
    else:
        recommendations = ["Analyze risk manually", "Monitor system closely"]

    rec_text = "\n- ".join([""] + recommendations)  # تنسيق التوصيات

    report = f"""
Risk: {risk_type}

Why it happened:
{cause}

Explanation:
{explanation_text}

Recommended actions:{rec_text}
"""
    return report

def summarize_results(results):
    """
    يحول قائمة النتائج إلى تقرير كامل واحد
    """
    final_report = "\n=== ACPPL AI Report Start ===\n"
    for r in results:
        final_report += explain_risk(r)
        final_report += "\n------------------------------\n"
    final_report += "=== ACPPL AI Report End ===\n"
    return final_report
