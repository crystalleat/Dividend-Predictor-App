import streamlit as st
import pandas as pd
st.title("📘 Financial Ratios we used")

st.markdown("""
This Dividend App leverages a combination of WRDS (Wharton Research Data Services) and real-time financials from yfinance to generate accurate and meaningful financial ratios.
-	WRDS / CRSP: 
                - Used for training data, historical dividend payout information, and standardized financial ratios from the Financial Ratios Suite by WRDS and CRSP (Center for Research in Security Prices).
                - The data cleaning included only keeping true dividend payment columns as well as relevant ratios. A new column was created to classify dividend changes as an increase, decrease, or no change based on the next quarter’s dividend. 
                - Each company was assigned an industry label based on the ticker. Missing values across key financial ratios were filled using ticker specific averages. 
                - Liquidity ratios were defaulted to zero for financial companies, as these firms typically do not report or rely on these ratios due to their business structure. 
-	yfinance: Used for live testing data. Financial ratios are calculated manually by combining line items from income statements, balance sheets, and cash flow statements.
These ratios provide insights into a company's dividend reliability, profitability, leverage, liquidity, cash flow health, and market valuation.

""")

st.title("📊 Financial Ratios Used in Prediction")

# Data
# Table Data
data = {
    "Short Name": [
        "DPR", "ROE", "ROA", "GProf", "NPM", "FCF/OCF", "Cash/Debt", "Cash/LT", "OCF/LTD",
        "TD/IC", "D/E", "Debt/EBITDA", "IntCov", "Current Ratio", "Cash Ratio", "Quick Ratio", "P/B"
    ],
    "Description": [
        "Dividend Payout Ratio", "Return on Equity", "Return on Assets", "Gross Profit Margin", "Net Profit Margin",
        "Free Cash Flow to Operating Cash Flow", "Cash to Total Debt Ratio", "Cash to Long-Term Debt Ratio",
        "Operating Cash Flow to Long-Term Debt", "Total Debt to Invested Capital Ratio", "Debt to Equity Ratio",
        "Debt to EBITDA Ratio", "Interest Coverage Ratio", "Current Ratio", "Cash Ratio", "Quick Ratio",
        "Price to Book Ratio (inverse form)"
    ],
    "Formula": [
        "cash_dividends_paid / net_income",
        "net_income / stockholders_equity",
        "net_income / total_assets",
        "gross_profit / total_revenue",
        "net_income / total_revenue",
        "free_cash_flow / operating_cash_flow",
        "cash_and_cash_equivalents / total_debt",
        "cash_and_cash_equivalents / long_term_debt",
        "operating_cash_flow / long_term_debt",
        "total_debt / invested_capital",
        "total_debt / stockholders_equity",
        "total_debt / ebitda",
        "ebit / interest_expense",
        "current_assets / current_liabilities",
        "cash_and_cash_equivalents / current_liabilities",
        "(current_assets - inventory) / current_liabilities",
        "stockholders_equity / total_assets"
    ]
}

# Render
df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)

# # Valuation
# st.header("📊 Valuation / Market")
# st.markdown("""
# - **Price-to-Book Proxy (P/B)**  
#   $$
#   \\text{P/B} = \\frac{\\text{Stockholders' Equity}}{\\text{Total Assets}}
#   $$
# """)
