import streamlit as st

st.title("About This App")

st.markdown("""
Welcome to the **Dividend Change Prediction App** — an interactive dashboard that forecasts whether a public company's dividend will:

- 📉 **Decrease**
- ➖ **Stay the Same**
- 📈 **Increase**

based on its **latest financial statement data**.

---

###  Project Objectives

- Leverage historical financial ratios to train predictive models
- Enable real-time predictions using data pulled from `yfinance`
- Provide clear explainability via classification reports, confusion matrices, and feature importance

---

### 🤖 Machine Learning Models Used

-  **XGBoost** — gradient-boosted trees
-  **CatBoost** — handles categorical + imbalanced data well
-  **LightGBM + Ensemble** — combined with logistic regression and decision trees for robustness

---

###  Features Engineered

Each model uses 16 key financial ratios, including:

- **Profitability:** ROE, ROA, Net Profit Margin, Gross Profit
- **Cash Flow:** FCF/OCF, Cash/Debt, OCF/LTD
- **Leverage:** Debt/Equity, Debt/EBITDA, Interest Coverage
- **Liquidity:** Current Ratio, Quick Ratio
- **Dividend Payout Ratio (DPR)**

---

### 🧾 Data Sources

- **Training Data:** WRDS / CRSP export merged with financial ratios
- **Test Data:** Live quarterly financials pulled using `yfinance`

---

### 📦 Tools & Libraries

- `streamlit`, `pandas`, `matplotlib`, `seaborn`
- `scikit-learn`, `xgboost`, `lightgbm`, `catboost`
- `yfinance` for dynamic company data

---

### 👩‍💻 Developed by

**Akshara Ramprasad** MSDS 2025
**Samritha Aadhi Ravikumar** MSDS 2025
**Crystal Leatvanich** 

---
""")
