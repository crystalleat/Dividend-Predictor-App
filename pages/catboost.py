# File: pages/catboost.py

import streamlit as st
import yfinance as yf
import pandas as pd
from catboost import CatBoostClassifier
import pickle
st.title("🐱 CatBoost Model with yFinance Test Data")

ticker = st.text_input("Enter Ticker Symbol (e.g., GE, MSFT):", value="GE")

if st.button("Predict with CatBoost"):
    try:
        stock = yf.Ticker(ticker)

        # Try getting quarterly financial statements
        income_stmt = stock.quarterly_income_stmt
        balance_sheet = stock.quarterly_balance_sheet
        cashflow_stmt = stock.quarterly_cashflow

        # Validate presence and content
        if (income_stmt is None or income_stmt.empty or 
            balance_sheet is None or balance_sheet.empty or 
            cashflow_stmt is None or cashflow_stmt.empty):
            st.warning("⚠️ Financial data not available or incomplete for this ticker.")
            st.stop()

        # Select the most recent column (latest quarter)
        income_stmt = income_stmt.iloc[:, 0]
        balance_sheet = balance_sheet.iloc[:, 0]
        cashflow_stmt = cashflow_stmt.iloc[:, 0]

        def safe_get(d, key):
            return d[key] if key in d else 0

        def safe_div(a, b):
            try:
                a = float(a)
                b = float(b)
                return a / b if b != 0 else 0
            except:
                return 0

        # Compute financial ratios
        ratios = {
            'dpr': safe_div(safe_get(cashflow_stmt, "Cash Dividends Paid"), safe_get(income_stmt, "Net Income")),
            'roe': safe_div(safe_get(income_stmt, "Net Income"), safe_get(balance_sheet, "Stockholders Equity")),
            'roa': safe_div(safe_get(income_stmt, "Net Income"), safe_get(balance_sheet, "Total Assets")),
            'GProf': safe_div(safe_get(income_stmt, "Gross Profit"), safe_get(income_stmt, "Total Revenue")),
            'npm': safe_div(safe_get(income_stmt, "Net Income"), safe_get(income_stmt, "Total Revenue")),
            'fcf_ocf': safe_div(safe_get(cashflow_stmt, "Free Cash Flow"), safe_get(cashflow_stmt, "Operating Cash Flow")),
            'cash_debt': safe_div(safe_get(balance_sheet, "Cash And Cash Equivalents"), safe_get(balance_sheet, "Total Debt")),
            'cash_lt': safe_div(safe_get(balance_sheet, "Cash And Cash Equivalents"), safe_get(balance_sheet, "Long Term Debt")),
            'ocf_lct': safe_div(safe_get(cashflow_stmt, "Operating Cash Flow"), safe_get(balance_sheet, "Long Term Debt")),
            'totdebt_invcap': safe_div(safe_get(balance_sheet, "Total Debt"), safe_get(balance_sheet, "Invested Capital")),
            'de_ratio': safe_div(safe_get(balance_sheet, "Total Debt"), safe_get(balance_sheet, "Stockholders Equity")),
            'debt_ebitda': safe_div(safe_get(balance_sheet, "Total Debt"), safe_get(income_stmt, "EBITDA")),
            'intcov_ratio': safe_div(safe_get(income_stmt, "EBIT"), safe_get(income_stmt, "Interest Expense")),
            'curr_ratio': safe_div(safe_get(balance_sheet, "Current Assets"), safe_get(balance_sheet, "Current Liabilities")),
            'cash_ratio': safe_div(safe_get(balance_sheet, "Cash And Cash Equivalents"), safe_get(balance_sheet, "Current Liabilities")),
            'quick_ratio': safe_div(
                safe_get(balance_sheet, "Current Assets") - safe_get(balance_sheet, "Inventory"),
                safe_get(balance_sheet, "Current Liabilities")
            ),
        }

        input_df = pd.DataFrame([ratios])
        st.subheader("📋 Computed Financial Ratios")
        st.dataframe(input_df.T)

        model = CatBoostClassifier()
        model.load_model("models/catboost_model.pkl")

        y_pred = model.predict(input_df)
        label_map = {-1: "📉 Decrease", 0: "➖ No Change", 1: "📈 Increase"}
        st.success(f"Prediction: **{label_map[int(y_pred[0])]}**")

    except Exception as e:
        st.error(f"Error: {e}")
