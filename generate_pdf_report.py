from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from acppl.ai_assistant import summarize_results

# أمثلة النتائج (يمكنك استبدالها بالنتائج الحقيقية من مكتبتك)
results = [
    {"risk": "brute_force", "cause": "150 failed login attempts", "explanation": "Multiple failed logins"},
    {"risk": "weak_passwords", "cause": "simple passwords used", "explanation": "Many weak passwords"},
    {"risk": "unusual_ip", "cause": "login from unknown country", "explanation": "IP from new place"},
    {"risk": "data_leak", "cause": "api keys exposed online", "explanation": "Secrets found in repos"}
]

# نحول النتائج إلى نص واحد
report_text = summarize_results(results)

# إنشاء PDF
pdf_file = "ACPPL_AI_Report.pdf"
c = canvas.Canvas(pdf_file, pagesize=A4)
width, height = A4

# كتابة النص على صفحات PDF
y = height - 50
for line in report_text.split("\n"):
    if y < 50:
        c.showPage()  # صفحة جديدة إذا انتهى الفراغ
        y = height - 50
    c.drawString(50, y, line)
    y -= 15  # تباعد بين الأسطر

c.save()
print(f"PDF generated: {pdf_file}")
