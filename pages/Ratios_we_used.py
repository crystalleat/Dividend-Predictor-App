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

data = [
    ("DPR", "Dividend Payout Ratio", r"$$\text{DPR} = \frac{\text{Cash Dividends Paid}}{\text{Net Income}}$$"),
    ("ROE", "Return on Equity", r"$$\text{ROE} = \frac{\text{Net Income}}{\text{Stockholders' Equity}}$$"),
    ("ROA", "Return on Assets", r"$$\text{ROA} = \frac{\text{Net Income}}{\text{Total Assets}}$$"),
    ("GProf", "Gross Profit Margin", r"$$\text{GProf} = \frac{\text{Gross Profit}}{\text{Total Revenue}}$$"),
    ("NPM", "Net Profit Margin", r"$$\text{NPM} = \frac{\text{Net Income}}{\text{Total Revenue}}$$"),
    ("FCF/OCF", "Free Cash Flow to Operating Cash Flow", r"$$\frac{\text{Free Cash Flow}}{\text{Operating Cash Flow}}$$"),
    ("Cash/Debt", "Cash to Total Debt Ratio", r"$$\frac{\text{Cash and Cash Equivalents}}{\text{Total Debt}}$$"),
    ("Cash/LT", "Cash to Long-Term Debt", r"$$\frac{\text{Cash and Cash Equivalents}}{\text{Long-Term Debt}}$$"),
    ("OCF/LTD", "OCF to Long-Term Debt", r"$$\frac{\text{Operating Cash Flow}}{\text{Long-Term Debt}}$$"),
    ("TD/IC", "Total Debt to Invested Capital", r"$$\frac{\text{Total Debt}}{\text{Invested Capital}}$$"),
    ("D/E", "Debt to Equity", r"$$\frac{\text{Total Debt}}{\text{Stockholders' Equity}}$$"),
    ("Debt/EBITDA", "Debt to EBITDA", r"$$\frac{\text{Total Debt}}{\text{EBITDA}}$$"),
    ("IntCov", "Interest Coverage Ratio", r"$$\frac{\text{EBIT}}{\text{Interest Expense}}$$"),
    ("Current Ratio", "Current Ratio", r"$$\frac{\text{Current Assets}}{\text{Current Liabilities}}$$"),
    ("Cash Ratio", "Cash Ratio", r"$$\frac{\text{Cash and Cash Equivalents}}{\text{Current Liabilities}}$$"),
    ("Quick Ratio", "Quick Ratio", r"$$\frac{\text{Current Assets} - \text{Inventory}}{\text{Current Liabilities}}$$"),
    ("P/B", "Price to Book (inverse)", r"$$\frac{\text{Stockholders' Equity}}{\text{Total Assets}}$$")
]

for short, desc, formula in data:
    st.markdown(f"""
**{short}** — *{desc}*  
{formula}
---
""")
# # Valuation
# st.header("📊 Valuation / Market")
# st.markdown("""
# - **Price-to-Book Proxy (P/B)**  
#   $$
#   \\text{P/B} = \\frac{\\text{Stockholders' Equity}}{\\text{Total Assets}}
#   $$
# """)
