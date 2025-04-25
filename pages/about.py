import streamlit as st

st.title("📘 Overview")

st.markdown("""
### Project Objectives

The application is designed to assist financial analysts and investors in evaluating dividend trends across industries. By leveraging historical financial data and machine learning, it aims to predict whether a company is likely to **increase**, **decrease**, or **maintain** its dividend payout. 

---

### Uses for a Dividend Prediction Model

- **Alerting System**: Real-time alerts for dividend payment likelihood based on new financial data.  
- **Comparative Analysis**: Rank companies within the same industry based on dividend probability.  
- **Portfolio Construction**: Select high-probability dividend-paying stocks for income-focused portfolios.  
- **Screening for Financial Health**: Use model insights to assess company financial stability.  

---

### Key Features

- **20 Years of Financial Ratios**: Trains predictive models using long-term financial metrics.  
- **Real-Time Prediction**: Live data fetched from Yahoo Finance using `yfinance`.  
- **Industry-Specific Modeling**: Custom models trained for sectors like **Financials**, **Consumer Discretionary**, and **Energy (Oil & Gas)**.  

---

### Machine Learning Models

- **XGBoost**: Gradient-boosted trees with high accuracy and efficiency.  
- **CatBoost**: Handles categorical variables and imbalanced data effectively.  
- **LightGBM + Ensemble**: Combines boosting with logistic regression and decision trees.  

---

### Data Sources

- **Training Data**: WRDS / CRSP export merged with financial ratios.  
- **Test Data**: Real-time financials pulled dynamically via `yfinance`.  

---

### Future Updates

- **Addressing Data Imbalance**: Future versions will refine sample selection to better balance classes.  
- **Expanded Industry & Global Coverage**: Include more sectors and international stocks.  
- **Model Monitoring & Alerts**: Add tools to track model drift and trigger alerts on drastic financial changes.  
""")

