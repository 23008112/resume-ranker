import streamlit as st
import fitz  # PyMuPDF
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Fast Resume Matcher", layout="wide")
st.title("🚀 Fast Resume Matcher")

@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

model = load_model()

def extract_text(pdf_bytes):
    txt = ""
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    for page in doc:
        txt += page.get_text()
    return txt

# 1) Upload resumes
uploaded = st.file_uploader(
    "📄 Upload Resumes (PDF, you can select multiple)",
    type="pdf",
    accept_multiple_files=True
)

# 2) Enter job description
jd = st.text_area("✏️ Paste the Job Description here", height=150)

if uploaded and jd.strip():
    with st.spinner("🔍 Processing…"):
        # Extract texts
        resumes = {f.name: extract_text(f.read()) for f in uploaded}

        # Prepare embeddings
        jd_emb = model.encode([jd])
        res_embs = model.encode(list(resumes.values()))

        # Compute similarities
        sims = cosine_similarity(jd_emb, res_embs)[0]
        ranked = sorted(zip(resumes.keys(), sims), key=lambda x: x[1], reverse=True)

    # 3) Display results
    st.subheader("🏅 Ranked Candidates")
    for name, score in ranked:
        st.markdown(f"**{name}** — Similarity: {score:.2f}")
        # Show a snippet from the resume
        snippet = resumes[name][:300].replace("\n", " ")
        st.write(f"> {snippet}…")
        st.write("---")
