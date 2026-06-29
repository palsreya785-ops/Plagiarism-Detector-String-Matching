# 📚 Plagiarism Detector Using String Matching Algorithms

## 📖 Overview

This project is a plagiarism detection system developed using Python, FastAPI, and classical string matching algorithms.

It compares two documents and calculates the plagiarism percentage by identifying similar words and sentences.

---

## 🚀 Features

- Upload two documents
- Supports TXT, DOCX and PDF
- Text preprocessing
- Naive String Matching
- KMP Algorithm
- Rabin-Karp Algorithm
- Sentence similarity detection
- Plagiarism percentage calculation
- FastAPI REST API
- Swagger UI

---

## 🛠 Technologies Used

- Python
- FastAPI
- Uvicorn
- PyPDF2
- python-docx
- Scikit-learn

---

## 📂 Project Structure

```
Plagiarism-Detector-String-Matching/
│
├── backend/
├── sample_documents/
├── screenshots/
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ⚙ Installation

```bash
git clone https://github.com/YOUR_USERNAME/Plagiarism-Detector-String-Matching.git

cd Plagiarism-Detector-String-Matching/backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python -m uvicorn app:app --reload
```

---

## API

Open

```
http://127.0.0.1:8000/docs
```

Upload:

- Original Document

- Submitted Document

Click **Execute**

---

## Algorithms Used

- Naive String Matching

- Knuth Morris Pratt (KMP)

- Rabin-Karp

---

## Sample Output

```
Overall Score : 72%

Risk Level : Medium

Matched Words

Artificial

Intelligence

Machine

Learning

Education
```

---

## Future Improvements

- Winnowing
- MinHash
- LSH
- React Dashboard
- HTML Reports
- PDF Reports

---

## Author

Sreya Pal
