from docx import Document
import PyPDF2
import os


def read_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def read_docx(path):
    doc = Document(path)
    text = ""

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text


def read_pdf(path):
    text = ""

    with open(path, "rb") as file:

        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text

    return text


def read_document(path):

    ext = os.path.splitext(path)[1].lower()

    if ext == ".txt":
        return read_txt(path)

    elif ext == ".docx":
        return read_docx(path)

    elif ext == ".pdf":
        return read_pdf(path)

    else:
        raise Exception("Unsupported File Type")