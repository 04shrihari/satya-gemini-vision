import os
import streamlit as st
from PIL import Image
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    st.error("❌ GOOGLE_API_KEY not found in .env file")
    st.stop()

genai.configure(api_key=GOOGLE_API_KEY)

# Set up Streamlit page
st.set_page_config(page_title="Gemini Invoice Analyzer", layout="centered")

# Custom CSS for pastel theme
st.markdown("""
    <style>
        .stApp {
            background-color: #fefaf6;
            color: #333;
        }
        h1 {
            color: #ff69b4;
            font-weight: bold;
        }
        .stTextInput>div>div>input {
            background-color: #fff0f5;
            color: #000;
            font-weight: bold;
        }
        .stFileUploader>div>div {
            background-color: #fffaf0;
            font-weight: bold;
        }
        .stButton>button {
            background-color: #ffb6c1;
            color: black;
            font-weight: bold;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🌸 Gemini Invoice Analyzer")

# Input: File and Question
uploaded_file = st.file_uploader("📤 Upload an Invoice Image", type=["jpg", "jpeg", "png"])
user_question = st.text_input("❓ What would you like to know about this invoice?")

# Display image preview
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="🖼️ Preview", use_column_width=True)

# Convert image to Gemini-compatible format
def get_image_parts(file):
    return [{
        "mime_type": file.type,
        "data": file.getvalue()
    }]

# Call Gemini 1.5 Flash model
def ask_gemini(question, image_parts):
    model = genai.GenerativeModel("models/gemini-1.5-flash")
    response = model.generate_content([question, image_parts[0]])
    return response.text

# Submit Button
if st.button("🔍 Analyze"):
    if not uploaded_file or not user_question:
        st.warning("Please upload an image and type a question.")
    else:
        try:
            image_data = get_image_parts(uploaded_file)
            with st.spinner("Thinking..."):
                output = ask_gemini(user_question, image_data)
            st.subheader("📋 Answer")
            st.write(output)
        except Exception as e:
            st.error(f"❌ Error: {e}")
