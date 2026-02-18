from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(df, output="results/report.pdf"):

    doc = SimpleDocTemplate(output)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("Protein Analysis Report", styles["Heading1"]))
    elements.append(Spacer(1,12))

    for _, row in df.head(5).iterrows():
        elements.append(
            Paragraph(f"{row['id']} — Score: {row['score']:.3f}",
                      styles["Normal"])
        )
        elements.append(Spacer(1,6))

    doc.build(elements)
