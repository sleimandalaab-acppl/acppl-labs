# ai_assistant.py

def explain_risk(risk):
    """
    يحول مخاطر ACPPL إلى تقرير مفصل قابل للقراءة.
    """
    explanation = f"""
Risk: {risk.get('risk', 'Unknown')}

Why it happened:
{risk.get('cause', 'Unknown')}

Explanation:
{risk.get('explanation', 'No further details')}

Recommended actions:
- Enable rate limiting
- Strengthen passwords
- Monitor unusual IPs
"""
    return explanation
