# File: app.py
import streamlit as st

# Set app config
st.set_page_config(page_title="Dividend Change Prediction App", layout="wide")

# Define all pages
App_page_0 = st.Page("pages/about.py", title="ℹ️ Overview")
App_page_1 = st.Page("pages/code.py", title="🌲 Codes for each Model")
App_page_2 = st.Page("pages/predict_from_yfinance.py", title="🧮 Predict from yFinance")
App_page_3 = st.Page("pages/main.py", title="🏠 Training Dataset", default=True)
App_page_4 = st.Page("pages/about_ratios.py", title="📘 Ratios we used")
App_page_5 = st.Page("pages/gpt_analysis.py", title="🤖 GPT Analysis")  # ✅ Added!

# Sidebar Navigation Groups
pg = st.navigation({
    "Start Here": [App_page_0],
    "Model Dashboards": [App_page_1, App_page_2],
    "Interpretation": [App_page_5],  # ✅ GPT explanation
    "More Info": [App_page_3, App_page_4],
})


st.sidebar.markdown("""
### Project Navigation
Use the sidebar to switch between models and view reports, confusion matrices, and export options.
""")

pg.run()
