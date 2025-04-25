# File: home.py
import streamlit as st

# st.set_page_config(
#     page_title="Dividend Trend Predictor",
#     page_icon="📈",
#     layout="wide"
# )
import streamlit as st

# Set page config
st.set_page_config(page_title="Home", layout="wide")

# Inject CSS for background image
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1454165804606-c3d57bc86b40");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📊 Dividend Trend Predictor")

st.markdown("""

<span style='font-size: 24px; font-weight: bold;'>BA870 Financial Analytics - Final Project</span>

<br>

Team Members:
- Akshara Ramprasad MSDS'25
- Samritha Aadhi Ravikumar MSDS'25
- Crystal Leatvanich MSBA'25
""", unsafe_allow_html=True)

