
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
## Output
<img width="1855" height="472" alt="image" src="https://github.com/user-attachments/assets/302c2eda-bf84-4f5c-8b18-2d8b47ef2e56" />
<img width="1789" height="234" alt="image" src="https://github.com/user-attachments/assets/fe275bc7-d4c9-4b3e-872b-89b3b12a7da3" />
<img width="1870" height="589" alt="image" src="https://github.com/user-attachments/assets/88e68d3c-6ea9-4df3-b604-d677da568dac" />


---

## 💡 Inspired by

Tools that simplify hiring by combining AI + resume parsing.

---


