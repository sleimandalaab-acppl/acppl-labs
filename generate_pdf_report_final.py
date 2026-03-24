from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.utils import ImageReader
from datetime import datetime
from acppl.ai_assistant import summarize_results

# بيانات اختبار
results = [
    {"risk": "brute_force", "cause": "150 failed login attempts", "explanation": "Multiple failed logins"},
    {"risk": "weak_passwords", "cause": "simple passwords used", "explanation": "Many weak passwords"},
    {"risk": "unusual_ip", "cause": "login from unknown country", "explanation": "IP from new place"},
    {"risk": "data_leak", "cause": "api keys exposed online", "explanation": "Secrets found in repos"}
]

report_texts = [r.strip() for r in summarize_results(results).split("------------------------------")]

pdf_file = "ACPPL_AI_Report_Final.pdf"
c = canvas.Canvas(pdf_file, pagesize=A4)
width, height = A4

# --- صفحة الغلاف ---
c.setFont("Helvetica-Bold", 24)
c.drawCentredString(width/2, height - 5*cm, "ACPPL AI Risk Report")
c.setFont("Helvetica", 14)
c.drawCentredString(width/2, height - 6*cm, f"Date: {datetime.now().strftime('%Y-%m-%d')}")

# إضافة شعار
try:
    logo = ImageReader("acppl_logo.png")
    c.drawImage(logo, width/2 - 4*cm, height - 9*cm, width=8*cm, height=4*cm, preserveAspectRatio=True)
except:
    print("Logo not found, skipping.")

c.showPage()

# --- صفحة جدول المحتويات ---
c.setFont("Helvetica-Bold", 18)
c.drawString(2*cm, height - 3*cm, "Table of Contents")
c.setFont("Helvetica", 12)
y = height - 4*cm
for i, report in enumerate(report_texts, start=1):
    risk_name = report.split("\n")[0].replace("Risk: ", "")
    c.drawString(2.5*cm, y, f"{i}. {risk_name}")
    c.drawString(15*cm, y, f"Page {i+2}")  # افتراض ترقيم الصفحات يبدأ من 3
    y -= 1*cm

c.showPage()

# --- صفحات التقرير ---
y = height - 3*cm
risk_colors = {
    "brute_force": colors.red,
    "weak_passwords": colors.orange,
    "unusual_ip": colors.blue,
    "data_leak": colors.green
}

page_num = 1
for report in report_texts:
    lines = report.split("\n")
    if not lines or len(lines) < 2:
        continue
    risk_line = lines[0].replace("Risk: ", "").lower()
    color = risk_colors.get(risk_line, colors.black)

    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(color)
    c.drawString(2*cm, y, lines[0])
    y -= 1*cm

    c.setFont("Helvetica", 11)
    c.setFillColor(colors.black)
    for line in lines[1:]:
        if line.strip() == "":
            continue
        if y < 3*cm:
            # ترقيم الصفحة
            c.setFont("Helvetica", 9)
            c.drawRightString(width - 2*cm, 1.5*cm, f"Page {page_num}")
            page_num += 1
            c.showPage()
            y = height - 3*cm
        c.drawString(2*cm, y, line)
        y -= 0.7*cm

    y -= 1*cm
    # ترقيم الصفحة بعد كل خطر
    c.setFont("Helvetica", 9)
    c.drawRightString(width - 2*cm, 1.5*cm, f"Page {page_num}")
    page_num += 1
    y = height - 3*cm

c.save()
print(f"Final professional PDF generated: {pdf_file}")
