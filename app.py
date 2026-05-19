import streamlit as st
from PIL import Image

from src.predict import load_asl_model, predict_asl_sign


st.set_page_config(
    page_title="ASL Sign Language Recognition",
    page_icon="✋",
    layout="wide"
)


st.markdown(
    """
    <style>
    .main {
        background-color: #f8fafc;
    }

    .title {
        font-size: 46px;
        font-weight: 800;
        color: #111827;
        text-align: center;
        margin-bottom: 10px;
    }

    .subtitle {
        font-size: 18px;
        color: #4b5563;
        text-align: center;
        margin-bottom: 35px;
    }

    .card {
        background-color: white;
        padding: 25px;
        border-radius: 18px;
        box-shadow: 0 4px 18px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }

    .result-box {
        background: linear-gradient(135deg, #2563eb, #7c3aed);
        color: white;
        padding: 30px;
        border-radius: 18px;
        text-align: center;
        margin-top: 20px;
    }

    .predicted-letter {
        font-size: 64px;
        font-weight: 900;
        margin: 10px 0;
    }

    .confidence {
        font-size: 22px;
        font-weight: 600;
    }

    .small-text {
        color: #6b7280;
        font-size: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


@st.cache_resource
def get_model():
    return load_asl_model()


model = get_model()


st.markdown(
    "<div class='title'>✋ Sign Language Recognition</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>AI system for recognizing American Sign Language hand gestures using CNN deep learning model</div>",
    unsafe_allow_html=True
)


left_col, right_col = st.columns([1, 1])


with left_col:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("📤 Upload Image")

    st.write(
        "Upload a hand gesture image. The system will analyze it and predict the ASL letter."
    )

    uploaded_file = st.file_uploader(
        "Choose an image",
        type=["jpg", "jpeg", "png"]
    )

    st.markdown(
        """
        <p class='small-text'>
        Supported formats: JPG, JPEG, PNG<br>
        Recommended: clear image with one hand gesture
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)


with right_col:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("ℹ️ About Project")

    st.write(
        """
        This project uses a Convolutional Neural Network to classify ASL alphabet gestures.
        The model was trained on the ASL Alphabet dataset from Kaggle.
        """
    )

    st.write("**Classes:** 29")
    st.write("**Task:** Multi-class image classification")
    st.write("**Model:** CNN")

    st.markdown("</div>", unsafe_allow_html=True)


if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")

    st.markdown("---")

    image_col, result_col = st.columns([1, 1])

    with image_col:
        st.subheader("🖼 Uploaded Image")
        st.image(image, use_container_width=True)

    with result_col:
        st.subheader("🤖 Prediction Result")

        predicted_class, confidence, top_3 = predict_asl_sign(model, image)

        st.markdown(
            f"""
            <div class='result-box'>
                <div>Predicted ASL Sign</div>
                <div class='predicted-letter'>{predicted_class}</div>
                <div class='confidence'>Confidence: {confidence:.2f}%</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("### Top 3 Predictions")

        for item in top_3:
            st.write(f"**{item['class']}** — {item['confidence']:.2f}%")
            st.progress(item["confidence"] / 100)


st.markdown("---")

st.markdown(
    """
    ### 🎯 Project Purpose

    This application demonstrates how deep learning can be used for accessibility technologies.
    It can recognize American Sign Language hand gestures from images and return the predicted letter.

    ### 🧠 Technologies Used

    Python · TensorFlow · Keras · CNN · Streamlit · Computer Vision
    """
)
