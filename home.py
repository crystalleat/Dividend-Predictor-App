# File: home.py
import streamlit as st

st.set_page_config(
    page_title="Dividend Change Predictor",
    page_icon="📈",
    layout="wide"
)

st.title("📊 Welcome to the Dividend Change Predictor App")

st.markdown("""
This app helps predict whether a company's dividend will:

- 📈 Increase  
- ➖ Stay the same  
- 📉 Decrease  

It uses financial ratios from **yFinance** and industry-specific machine learning models.

---

### 🔍 Explore via the sidebar:
- 🧮 Make a prediction using real-time stock data
- 🤖 View GPT-style natural language analysis
- 📘 Learn the formulas and logic used
- 🔢 See how the models were trained

Built with ❤️ using Streamlit, Scikit-learn, LightGBM, and XGBoost.
""")
