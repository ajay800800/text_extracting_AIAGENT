

# 🧠 PDF/Text Extractor Agent – Full Stack

A full-stack application (React + Node.js + Python) for uploading PDF, DOCX, or scanned documents and extracting text content using an AI-powered backend. Ideal for intelligent document understanding, search, summarization, and multi-agent orchestration.

---

## 🔧 Technologies Used

- 📦 **Frontend**: React (with file upload)
- 🚀 **Backend**: Node.js (Express server)
- 🐍 **Text Extraction**:
  - **PyMuPDF**: High-performance PDF text extraction
  - **pytesseract**: OCR for scanned PDFs
  - **Pillow**: Image processing for OCR
  - **python-docx**: DOCX file text extraction
  - **libreoffice**: Convert documents to PDF (optional, for broader format support)
- 🔗 **Communication**: REST API

---

## 📁 Folder Structure

```
pdf-text-extractor/
├── backend/
│   ├── server.js              # Node.js Express API
│   ├── extract_text.py        # Python Flask server for text extraction
│   ├── uploads/               # Temporary storage for uploaded files
│   ├── extracted/             # (Optional) Store extracted outputs
│   └── requirements.txt       # Python dependencies
├── frontend/
│   ├── public/
│   └── src/
│       ├── App.js             # Main UI
│       ├── UploadForm.js      # File input form
│       └── index.js
├── README.md
└── package.json
```

---

## ⚙️ Setup Instructions

### 🔌 1. Clone the Repository

```bash
git clone https://github.com/your-username/pdf-text-extractor.git
cd pdf-text-extractor
```

### 🐍 2. Start the Python Extractor

Install Python dependencies and run the text extractor service:

```bash
cd backend
pip install flask PyMuPDF pytesseract Pillow python-docx
# Install Tesseract OCR: e.g., `sudo apt install tesseract-ocr` (Ubuntu)
# Install LibreOffice if needed: e.g., `sudo apt install libreoffice` (Ubuntu)
python3 extract_text.py
```

- **Runs on**: `http://localhost:5000`
- **Note**: Ensure Tesseract OCR is installed for `pytesseract` (e.g., `sudo apt install tesseract-ocr` on Ubuntu).

### 🔧 3. Start the Node Backend

In a second terminal:

```bash
cd backend
npm install
node server.js
```

- **Runs on**: `http://localhost:3000`

### 💻 4. Start the React Frontend

In a third terminal:

```bash
cd frontend
npm install
npm start
```

- **Runs on**: `http://localhost:5173` (Vite) or `http://localhost:3001` (Create React App)

### 🧪 How It Works

1. Upload a `.pdf`, `.docx`, or scanned document via the React UI.
2. Node.js receives the file and forwards it to the Python extractor.
3. Python processes the file:
   - **PDFs**: Extract text using `PyMuPDF` or perform OCR with `pytesseract` (using `Pillow` for image processing).
   - **DOCX**: Extract text using `python-docx`.
   - **Other formats**: Convert to PDF using `libreoffice` (if supported) before extraction.
4. Extracted text is returned to the Node.js backend and displayed in the UI.

---

## 🖼️ Demo Screenshot

*(Insert a screenshot here if available)*

---

## 🛠️ Example API Request

Upload a file using cURL:

```bash
curl -X POST http://localhost:3000/extract-text \
  -F "file=@sample.pdf"
```

---

## 💡 Future Enhancements

- Add summarization using LLMs (e.g., via xAI's Grok API).
- Convert extracted text to structured JSON (e.g., tables, headings).
- Support additional formats (e.g., TXT, RTF).
- Improve OCR accuracy for complex scanned documents.
- Implement history/session management for user uploads.

---

## 📄 License

MIT License © 2025 ajay panchal

