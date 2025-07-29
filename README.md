
# 🚀 Fast Resume Matcher

A simple and fast resume ranking tool built with Streamlit and Sentence Transformers. Upload multiple resumes (PDF), paste a job description, and get ranked candidates based on semantic similarity.

## 🔍 Features

- 📄 Upload multiple PDF resumes
- ✏️ Paste a job description to match against
- ⚡ Fast semantic similarity using `all-MiniLM-L6-v2`
- 🧠 Powered by Sentence Transformers
- 📊 Ranked output with resume snippet previews

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) — Interactive web UI
- [Sentence Transformers](https://www.sbert.net/) — For semantic embedding
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/) — PDF text extraction
- [scikit-learn](https://scikit-learn.org/) — Cosine similarity calculation

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/fast-resume-matcher.git
cd fast-resume-matcher
````

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
streamlit run app.py
```

---

## 📂 File Structure

```
fast-resume-matcher/
│
├── app.py               # Main Streamlit app
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## ✅ Requirements

* Python 3.7+
* PDF resumes (only `.pdf` supported)
* Internet connection (for model download)

---

## 📦 Example `requirements.txt`

```
txt
streamlit
sentence-transformers
scikit-learn
PyMuPDF
```

---

## 💡 Inspired by

Tools that simplify hiring by combining AI + resume parsing.

---


