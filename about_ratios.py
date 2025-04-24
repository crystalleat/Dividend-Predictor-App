import streamlit as st

st.title("📘 Financial Ratios we used")

st.markdown("""
Below are the financial ratios used in our dividend prediction models, categorized by their type.
""")

# Target / Outcome
st.header("🎯 Target / Outcome")
st.markdown("""
- **Dividend Payout Ratio (DPR)**  
  $$
  \\text{DPR} = \\frac{\\text{Cash Dividends Paid}}{\\text{Net Income}}
  $$
""")

# Profitability
st.header("💰 Profitability Ratios")
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
st.header("💵 Cash Flow Ratios")
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
st.header("📉 Leverage Ratios")
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
st.header("💧 Liquidity Ratios")
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
st.header("📊 Valuation / Market")
st.markdown("""
- **Price-to-Book Proxy (P/B)**  
  $$
  \\text{P/B} = \\frac{\\text{Stockholders' Equity}}{\\text{Total Assets}}
  $$
""")
