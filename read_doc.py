from docx import Document

doc = Document('ADR_500.docx')
for p in doc.paragraphs:
    print(p.text)
