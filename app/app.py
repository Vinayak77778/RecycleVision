import sys
import os
import io
from PIL import Image
import streamlit as st

# Path setup
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.predict import classify_image
from src.category_mapper import map_to_category

# ---- Page config ----
st.set_page_config(
    page_title="RecycleVision – Waste Classifier",
    page_icon="♻️",
    layout="centered",
)

# ---- Custom styles ----
st.markdown("""
    <style>
        html, body {
            background-color: #f4f7f6;
            font-family: 'Segoe UI', sans-serif;
        }

        .main-title {
            font-size: 2.4em;
            color: #2e7d32;
            text-align: center;
            font-weight: bold;
            margin-bottom: 10px;
        }

        .subtitle {
            font-size: 1.1em;
            text-align: center;
            color: #444;
            margin-bottom: 30px;
        }

        .prediction-box {
            font-size: 1.2em;
            font-weight: bold;
            color: #1b5e20;
            background-color: #c8e6c9;
            padding: 12px;
            border-radius: 10px;
            margin-top: 25px;
            text-align: center;
        }

        footer {
            text-align: center;
            font-size: 0.85em;
            color: #999;
            margin-top: 50px;
        }

        /* Hide file name display */
        [data-testid="uploaded-file-name"] {
            display: none !important;
        }

        [data-testid="stFileUploader"] div[aria-live="polite"] {
            visibility: hidden;
            height: 0;
            overflow: hidden;
        }
    </style>
""", unsafe_allow_html=True)

# ---- Title ----
st.markdown('<div class="main-title">♻️ RecycleVision – Waste Classifier</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Upload an image of a waste item to classify it as recyclable, compostable, or non-recyclable.</div>', unsafe_allow_html=True)

# ---- Sidebar ----
with st.sidebar:
    st.title("ℹ️ About")
    st.write("""
    **RecycleVision** is a smart AI-powered web app that detects the recyclability of waste items 
    using the Clarifai General Image Recognition API.

    🌍 **Goal:** Support **SDG 12** – Responsible Consumption and Production  
    🛠️ **Built With:** Python, Streamlit, Clarifai API  
    🤖 **How it Works:** Upload an image and the app predicts its category based on image recognition.

    Ideal for education, awareness, and smart waste sorting.
    """)
    st.markdown("🔗 [Clarifai Website](https://www.clarifai.com)")

# ---- Upload section (no filename shown) ----
uploaded_file = st.file_uploader("📤 Upload an image", type=["jpg", "jpeg", "png"], label_visibility="collapsed")

if uploaded_file:
    # Convert to PIL image
    file_bytes = uploaded_file.read()
    image = Image.open(io.BytesIO(file_bytes))

    # Show image preview
    st.markdown('<div style="text-align:center;"><h4>🖼️ Uploaded Image</h4></div>', unsafe_allow_html=True)
    st.image(image, use_container_width=True)

    # Save image temporarily for prediction
    temp_path = os.path.join("static", "temp.jpg")
    os.makedirs("static", exist_ok=True)
    image.save(temp_path)

    try:
        labels = classify_image(temp_path)
        category = map_to_category(labels)

        # Show result
        st.markdown(f'<div class="prediction-box">🧾 Predicted Category: <strong>{category}</strong></div>', unsafe_allow_html=True)

    except Exception as e:
        st.error(f"🚫 Error: {e}")

    # Clean up temp image
    os.remove(temp_path)

# ---- Footer ----
st.markdown("""
    <footer>Made with ❤️ using Streamlit and Clarifai API • © 2025</footer>
""", unsafe_allow_html=True)
