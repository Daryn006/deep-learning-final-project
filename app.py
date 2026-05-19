import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
from src.predict import (
    load_asl_model,
    preprocess_image,
    predict_sign
)

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="ASL Recognition",
    page_icon="✋",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.title {
    text-align: center;
    font-size: 60px;
    font-weight: 800;
    color: #111827;
    margin-top: 20px;
}

.subtitle {
    text-align: center;
    font-size: 22px;
    color: #4b5563;
    margin-bottom: 40px;
}

.card {
    background: white;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.metric-card {
    background: linear-gradient(135deg, #2563eb, #1e40af);
    color: white;
    padding: 25px;
    border-radius: 18px;
    text-align: center;
}

.result-box {
    background: linear-gradient(135deg, #10b981, #059669);
    padding: 30px;
    border-radius: 20px;
    color: white;
    text-align: center;
    font-size: 32px;
    font-weight: bold;
}

.footer {
    text-align: center;
    color: gray;
    margin-top: 50px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------

st.markdown(
    '<div class="title">✋ Sign Language Recognition</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Deep Learning CNN system for recognizing American Sign Language gestures</div>',
    unsafe_allow_html=True
)

# ---------------- METRICS ----------------

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric-card">
        <h2>29</h2>
        <p>Classes</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <h2>CNN</h2>
        <p>Model Type</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <h2>AI</h2>
        <p>Computer Vision</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ---------------- LOAD MODEL ----------------

@st.cache_resource
def get_model():
    return load_asl_model()

model = get_model()

# ---------------- MAIN CONTENT ----------------

left, right = st.columns([1.1, 1])

# ---------------- LEFT SIDE ----------------

with left:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📤 Upload Hand Gesture Image")

    uploaded_file = st.file_uploader(
        "Choose image",
        type=["jpg", "jpeg", "png"]
    )

    st.caption("Supported formats: JPG, JPEG, PNG")

    if uploaded_file is not None:

        image = Image.open(uploaded_file)

        st.image(
            image,
            caption="Uploaded Image",
            use_container_width=True
        )

        with st.spinner("Analyzing gesture..."):

            predicted_class, confidence, probs = predict_sign(
                model,
                image
            )

        st.write("")

        st.markdown(f"""
        <div class="result-box">
            Prediction: {predicted_class}<br>
            Confidence: {confidence:.2f}%
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        st.subheader("📊 Top Predictions")

        top_indices = np.argsort(probs)[::-1][:5]

        class_names = [
            "A","B","C","D","E","F","G","H","I","J",
            "K","L","M","N","O","P","Q","R","S","T",
            "U","V","W","X","Y","Z",
            "del","nothing","space"
        ]

        for idx in top_indices:
            st.progress(float(probs[idx]))
            st.write(
                f"{class_names[idx]} — {probs[idx]*100:.2f}%"
            )

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- RIGHT SIDE ----------------

with right:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📘 About Project")

    st.write("""
This project uses a Convolutional Neural Network (CNN)
to recognize American Sign Language hand gestures.

The model was trained on the ASL Alphabet dataset
from Kaggle using TensorFlow and Keras.

The system can classify 29 gesture classes,
including alphabet letters and special symbols.
""")

    st.subheader("🧠 Technologies")

    st.write("""
- Python
- TensorFlow / Keras
- Streamlit
- Computer Vision
- Deep Learning
- CNN Architecture
""")

    st.subheader("🎯 Project Goal")

    st.write("""
The purpose of this project is to demonstrate
how artificial intelligence can improve accessibility
and communication technologies for people
who use sign language.
""")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- FOOTER ----------------

st.markdown("""
<div class="footer">
Final Deep Learning Project • ASL Recognition System
</div>
""", unsafe_allow_html=True)
