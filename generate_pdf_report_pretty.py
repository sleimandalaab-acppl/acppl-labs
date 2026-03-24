from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
from acppl.ai_assistant import summarize_results

styles = getSampleStyleSheet()

# بيانات اختبار
results = [
    {"risk": "brute_force", "cause": "150 failed login attempts", "explanation": "Multiple failed logins"},
    {"risk": "weak_passwords", "cause": "simple passwords used", "explanation": "Many weak passwords"},
    {"risk": "unusual_ip", "cause": "login from unknown country", "explanation": "IP from new place"},
    {"risk": "data_leak", "cause": "api keys exposed online", "explanation": "Secrets found in repos"}
]

doc = SimpleDocTemplate("ACPPL_AI_Report_Pro.pdf", pagesize=A4)
elements = []

# --- غلاف ---
elements.append(Paragraph("<b>ACPPL AI Risk Report</b>", styles['Title']))
elements.append(Spacer(1, 20))
elements.append(Paragraph(f"Date: {datetime.now().strftime('%Y-%m-%d')}", styles['Normal']))
elements.append(Spacer(1, 40))

# محاولة إضافة الشعار
try:
    elements.append(Image("acppl_logo.png", width=200, height=100))
except:
    pass

elements.append(Spacer(1, 50))

# --- التقرير ---
report_texts = [r.strip() for r in summarize_results(results).split("------------------------------")]

for report in report_texts:
    lines = report.split("\n")
    if len(lines) < 2:
        continue

    risk = lines[0].replace("Risk: ", "")
    cause = ""
    explanation = ""
    recommendations = []

    section = ""
    for line in lines:
        if "Why it happened" in line:
            section = "cause"
        elif "Explanation" in line:
            section = "explanation"
        elif "Recommended actions" in line:
            section = "rec"
        elif line.strip() == "":
            continue
        else:
            if section == "cause":
                cause += line + " "
            elif section == "explanation":
                explanation += line + " "
            elif section == "rec":
                recommendations.append(line)

    # جدول لكل خطر
    data = [
        ["Risk", risk],
        ["Cause", cause],
        ["Explanation", explanation],
        ["Recommendations", "\n".join(recommendations)]
    ]

    table = Table(data, colWidths=[120, 330])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("BOX", (0, 0), (-1, -1), 1, colors.black),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))

    elements.append(table)
    elements.append(Spacer(1, 25))

# بناء الملف
doc.build(elements)

print("Professional Report Created: ACPPL_AI_Report_Pro.pdf")
