import os
import subprocess
from PIL import Image
import pytesseract
import fitz  # PyMuPDF
from docx import Document
def extract_text_from_pdf(path):
    import tempfile

    doc = fitz.open(path)
    full_text = ""

    for i, page in enumerate(doc):
        print(f"Processing page {i+1}...")
        text = page.get_text()
        if text.strip():
            print("✅ Text found without OCR")
            full_text += text
        else:
            print("⚠️ No text found — using OCR...")
            # Render the page as an image and OCR it
            pix = page.get_pixmap(dpi=300)  # Higher DPI = better OCR accuracy
            image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

            # Optional: save image for debugging
            with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
                image.save(tmp.name)
                print(f"🖼️ Saved OCR image for debug: {tmp.name}")

            ocr_text = pytesseract.image_to_string(image)
            full_text += ocr_text

    return full_text or "[No text found in PDF]"


def extract_text_from_image(path):
    image = Image.open(path)
    return pytesseract.image_to_string(image)

def extract_text_from_docx(path):
    try:
        doc = Document(path)
        content = "\n".join(para.text for para in doc.paragraphs if para.text.strip())
        if content.strip():
            return content
        else:
            # If it's image-based (e.g., pasted image), fallback to OCR
            return ocr_docx_images(path)
    except Exception as e:
        return f"[DOCX Error] {e}"

def ocr_docx_images(path):
    from zipfile import ZipFile
    import io
    text = ""
    with ZipFile(path, 'r') as docx:
        for name in docx.namelist():
            if name.startswith('word/media/') and name.endswith(('.png', '.jpg', '.jpeg')):
                with docx.open(name) as img_file:
                    image = Image.open(io.BytesIO(img_file.read()))
                    text += pytesseract.image_to_string(image) + "\n"
    return text or "[No text or image content found in DOCX]"

def convert_doc_to_docx(path):
    try:
        subprocess.run(['libreoffice', '--headless', '--convert-to', 'docx', path], check=True)
        return path.replace('.doc', '.docx')
    except Exception as e:
        return None

def extract_text_auto(file_path):
    if not os.path.exists(file_path):
        return "❌ File not found."

    ext = os.path.splitext(file_path)[1].lower()
    print(f"[DEBUG] Path: {file_path}")
    print(f"[DEBUG] Ext: {ext}")


    try:
        if ext == '.pdf':
            return extract_text_from_pdf(file_path)

        elif ext in ['.png', '.jpg', '.jpeg']:
            return extract_text_from_image(file_path)

        elif ext == '.docx':
            return extract_text_from_docx(file_path)

        elif ext == '.doc':
            print("Converting .doc to .docx...")
            docx_path = convert_doc_to_docx(file_path)
            if docx_path and os.path.exists(docx_path):
                return extract_text_from_docx(docx_path)
            else:
                return "[Error converting .doc to .docx]"

        else:
            return f"[Unsupported file type: {ext}]"
    except Exception as e:
        return f"[Error during extraction: {e}]"

# --- Entry Point ---
if __name__ == "__main__":
    import sys
    path = sys.argv[1]
    print(extract_text_auto(path))
