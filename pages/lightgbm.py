# File: pages/lightgbm_ensemble.py
import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import pickle

st.title("💡 LightGBM + Ensemble with yFinance Test Data")

ticker = st.text_input("Enter Ticker Symbol (e.g., TSLA, GE):", value="GE")

if st.button("Predict with Ensemble"):
    try:
        stock = yf.Ticker(ticker)
        income_stmt = stock.quarterly_income_stmt.iloc[:, 0]
        balance_sheet = stock.quarterly_balance_sheet.iloc[:, 0]
        cashflow_stmt = stock.quarterly_cashflow.iloc[:, 0]

        def safe_div(a, b): return float(a)/float(b) if a and b and b != 0 else 0

        ratios = {
            'dpr': safe_div(cashflow_stmt.get("Cash Dividends Paid"), income_stmt.get("Net Income")),
            'roe': safe_div(income_stmt.get("Net Income"), balance_sheet.get("Stockholders Equity")),
            'roa': safe_div(income_stmt.get("Net Income"), balance_sheet.get("Total Assets")),
            'GProf': safe_div(income_stmt.get("Gross Profit"), income_stmt.get("Total Revenue")),
            'npm': safe_div(income_stmt.get("Net Income"), income_stmt.get("Total Revenue")),
            'fcf_ocf': safe_div(cashflow_stmt.get("Free Cash Flow"), cashflow_stmt.get("Operating Cash Flow")),
            'cash_debt': safe_div(balance_sheet.get("Cash And Cash Equivalents"), balance_sheet.get("Total Debt")),
            'cash_lt': safe_div(balance_sheet.get("Cash And Cash Equivalents"), balance_sheet.get("Long Term Debt")),
            'ocf_lct': safe_div(cashflow_stmt.get("Operating Cash Flow"), balance_sheet.get("Long Term Debt")),
            'totdebt_invcap': safe_div(balance_sheet.get("Total Debt"), balance_sheet.get("Invested Capital")),
            'de_ratio': safe_div(balance_sheet.get("Total Debt"), balance_sheet.get("Stockholders Equity")),
            'debt_ebitda': safe_div(balance_sheet.get("Total Debt"), income_stmt.get("EBITDA")),
            'intcov_ratio': safe_div(income_stmt.get("EBIT"), income_stmt.get("Interest Expense")),
            'curr_ratio': safe_div(balance_sheet.get("Current Assets"), balance_sheet.get("Current Liabilities")),
            'cash_ratio': safe_div(balance_sheet.get("Cash And Cash Equivalents"), balance_sheet.get("Current Liabilities")),
            'quick_ratio': safe_div(balance_sheet.get("Current Assets") - balance_sheet.get("Inventory"), balance_sheet.get("Current Liabilities")),
        }

        input_df = pd.DataFrame([ratios])
        st.subheader("📋 Computed Financial Ratios")
        st.dataframe(input_df.T)

        with open("models/ensemble_model.pkl", "rb") as f:
            model = pickle.load(f)

        y_pred = model.predict(input_df)
        label_map = {-1: "📉 Decrease", 0: "➖ No Change", 1: "📈 Increase"}
        st.success(f"Prediction: **{label_map[int(y_pred[0])]}**")

    except Exception as e:
        st.error(f"Error: {e}")