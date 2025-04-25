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

st.set_page_config(page_title="Home", layout="wide")

# Responsive background + text color based on system theme
st.markdown("""
<style>
/* Background styling */
.stApp {
    background-image: url('https://images.unsplash.com/photo-1581090700227-1e8a4b9dc1e5?auto=format&fit=crop&w=1470&q=80');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

/* Light mode: dark text on light background */
@media (prefers-color-scheme: light) {
    .custom-header {
        color: #111111;
        font-size: 24px;
        font-weight: bold;
    }
    .team-names {
        color: #222222;
    }
}

/* Dark mode: light text on dark background */
@media (prefers-color-scheme: dark) {
    .custom-header {
        color: #ffffff;
        font-size: 24px;
        font-weight: bold;
    }
    .team-names {
        color: #dddddd;
    }
}
</style>
""", unsafe_allow_html=True)

# Render content with classes
st.title("📊 Dividend Trend Predictor")

st.markdown("""
<div class="custom-header">BA870 Financial Analytics - Final Project</div>
<br>
<div class="team-names">
<ul>
  <li>Akshara Ramprasad MSDS'25</li>
  <li>Samritha Aadhi Ravikumar MSDS'25</li>
  <li>Crystal Leatvanich MSBA'25</li>
</ul>
</div>
""", unsafe_allow_html=True)
