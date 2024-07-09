import PyPDF2 as pdf

def cnv_pdf_to_text(uploaded_pdf)-> str:
    reader=pdf.PdfReader(uploaded_pdf)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text