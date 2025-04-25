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

st.header("📊 Financial Ratios Used in Prediction")

# Target / Outcome
st.markdown("#### Target / Outcome")
st.markdown("""
- **Dividend Payout Ratio (DPR)**  
  $$
  \\text{DPR} = \\frac{\\text{Cash Dividends Paid}}{\\text{Net Income}}
  $$
""")

# Profitability
st.subheader("Profitability Ratios")
st.markdown("""
- **Return on Equity (ROE)**  
  $$
  \\text{ROE} = \\frac{\\text{Net Income}}{\\text{Stockholders' Equity}}
  $$

- **Return on Assets (ROA)**  
  $$
  \\text{ROA} = \\frac{\\text{Net Income}}{\\text{Total Assets}}
  $$

- **Gross Profit Margin (GProf)**  
  $$
  \\text{GProf} = \\frac{\\text{Gross Profit}}{\\text{Total Revenue}}
  $$

- **Net Profit Margin (NPM)**  
  $$
  \\text{NPM} = \\frac{\\text{Net Income}}{\\text{Total Revenue}}
  $$
""")

# Cash Flow
st.subheader("💵 Cash Flow Ratios")
st.markdown("""
- **Free Cash Flow to Operating Cash Flow (FCF/OCF)**  
  $$
  \\text{FCF/OCF} = \\frac{\\text{Free Cash Flow}}{\\text{Operating Cash Flow}}
  $$

- **Cash to Total Debt**  
  $$
  \\text{Cash/Total Debt} = \\frac{\\text{Cash and Cash Equivalents}}{\\text{Total Debt}}
  $$

- **Cash to Long-Term Debt**  
  $$
  \\text{Cash/LT Debt} = \\frac{\\text{Cash and Cash Equivalents}}{\\text{Long-Term Debt}}
  $$

- **Operating Cash Flow to Long-Term Debt**  
  $$
  \\text{OCF/LT Debt} = \\frac{\\text{Operating Cash Flow}}{\\text{Long-Term Debt}}
  $$
""")

# Leverage
st.subheader("📉 Leverage Ratios")
st.markdown("""
- **Total Debt to Invested Capital**  
  $$
  \\text{Total Debt/InvCap} = \\frac{\\text{Total Debt}}{\\text{Invested Capital}}
  $$

- **Debt to Equity Ratio (D/E)**  
  $$
  \\text{D/E} = \\frac{\\text{Total Debt}}{\\text{Stockholders' Equity}}
  $$

- **Debt to EBITDA**  
  $$
  \\text{Debt/EBITDA} = \\frac{\\text{Total Debt}}{\\text{EBITDA}}
  $$

- **Interest Coverage Ratio**  
  $$
  \\text{IntCov} = \\frac{\\text{EBIT}}{\\text{Interest Expense}}
  $$
""")

# Liquidity
st.subheader("💧 Liquidity Ratios")
st.markdown("""
- **Current Ratio**  
  $$
  \\text{Current Ratio} = \\frac{\\text{Current Assets}}{\\text{Current Liabilities}}
  $$

- **Cash Ratio**  
  $$
  \\text{Cash Ratio} = \\frac{\\text{Cash and Cash Equivalents}}{\\text{Current Liabilities}}
  $$

- **Quick Ratio**  
  $$
  \\text{Quick Ratio} = \\frac{\\text{Current Assets} - \\text{Inventory}}{\\text{Current Liabilities}}
  $$
""")

# Valuation
st.subheader("📊 Valuation / Market")
st.markdown("""
- **Price-to-Book Proxy (P/B)**  
  $$
  \\text{P/B} = \\frac{\\text{Stockholders' Equity}}{\\text{Total Assets}}
  $$
""")
