# # File: home.py
# import streamlit as st
# st.set_page_config(page_title="Home", layout="wide")

# # Inject custom CSS for dark background image
# st.markdown(
#     """
#     <style>
#     .stApp {
#         background-image: url('https://images.unsplash.com/photo-1508780709619-79562169bc64');
#         background-size: cover;
#         background-position: center;
#         background-repeat: no-repeat;
#         background-attachment: fixed;
#     }

#     /* Optional: make main content darker for better readability */
#     .main {
#         background-color: rgba(0, 0, 0, 0.6);
#         padding: 2rem;
#         border-radius: 10px;
#     }

#     /* Optional: style titles */
#     h1 {
#         color: white;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# st.title("📊 Dividend Trend Predictor")

# st.markdown("""

# <span style='font-size: 24px; font-weight: bold;'>BA870 Financial Analytics - Final Project</span>

# <br>

# Team Members:
# - Akshara Ramprasad MSDS'25
# - Samritha Aadhi Ravikumar MSDS'25
# - Crystal Leatvanich MSBA'25
# """, unsafe_allow_html=True)

import streamlit as st

# Set page configuration
st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

# --- Background image and box CSS ---
page_bg_img = '''
<style>
.stApp {
    background-image: url('https://www.pristinemarketinsights.com/assets/images/banking-and-finance-bg.jpg');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

/* Transparent left-aligned box */
.transparent-box {
    background-color: rgba(0, 0, 0, 0.1);
    padding: 1.5rem 2rem;
    border-radius: 10px;
    width: 60%;
    margin: 1rem 0 2rem 1rem;
}

.transparent-box h1 {
    color: white;
    font-size: 36px;
}
.transparent-box h2 {
    color: white;
    font-size: 24px;
}
.transparent-box ul {
    list-style-type: none;
    padding-left: 1rem;
}
.transparent-box li {
    color: white;
    font-size: 18px;
    margin-bottom: 0.5rem;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# --- Render content ---
st.markdown("""
<div class="transparent-box">
    <h1>📊 Dividend Trend Predictor</h1>
    <h2>BA870 Financial Analytics - Final Project</h2>
    <br>
    <h4>Team Members:</h4>
    <ul>
        <li>- Akshara Ramprasad MSDS'25</li>
        <li>- Samritha Aadhi Ravikumar MSDS'25</li>
        <li>- Crystal Leatvanich MSBA'25</li>
    </ul>
</div>
""", unsafe_allow_html=True)
