# import streamlit as st

# st.title("🧠 GPT-Style Analysis of Dividend Prediction")

# # Check for required session variables
# if "prediction_label" not in st.session_state or "input_df" not in st.session_state:
#     st.warning("⚠️ Please run a prediction first using the 'Predict from yFinance' page.")
#     st.stop()

# label = st.session_state.prediction_label
# ratios = st.session_state.input_df.iloc[0].to_dict()
# ticker = st.session_state.get("ticker", "N/A")
# industry = st.session_state.get("industry", "Unknown")

# st.markdown(f"### Ticker: `{ticker}` | Industry: `{industry}`")
# st.markdown(f"### 📊 Predicted Dividend Change: **{label}**")

# # GPT-style explanation logic
# if label == "📈 Increase":
#     st.success(
#         """The model expects a dividend **increase**. This is likely supported by high profitability indicators such as:
# - Return on Equity (ROE): {:.2f}  
# - Net Profit Margin (NPM): {:.2f}  
# - Free Cash Flow / Operating Cash Flow: {:.2f}

# Additionally, liquidity metrics like the Quick Ratio ({:.2f}) and Cash Ratio ({:.2f}) suggest the company is well-positioned to distribute earnings."""
#         .format(
#             ratios.get('roe', 0),
#             ratios.get('npm', 0),
#             ratios.get('fcf_ocf', 0),
#             ratios.get('quick_ratio', 0),
#             ratios.get('cash_ratio', 0)
#         )
#     )
# elif label == "📉 Decrease":
#     st.warning(
#         """The model forecasts a **decrease** in dividends. Possible contributing factors:
# - Interest Coverage Ratio: {:.2f}  
# - Debt/EBITDA: {:.2f}  
# - Debt-to-Equity Ratio: {:.2f}  
# - Weak Profitability (ROE: {:.2f}, NPM: {:.2f})

# These suggest financial strain or a conservative capital structure."""
#         .format(
#             ratios.get('intcov_ratio', 0),
#             ratios.get('debt_ebitda', 0),
#             ratios.get('de_ratio', 0),
#             ratios.get('roe', 0),
#             ratios.get('npm', 0)
#         )
#     )
# else:
#     st.info(
#         """The dividend is expected to remain **unchanged**. This likely reflects a stable but conservative financial position:
# - Net Profit Margin: {:.2f}  
# - Return on Assets: {:.2f}  
# - Operating Cash Flow to Long-Term Debt: {:.2f}

# These indicators support maintaining, rather than increasing or decreasing, dividend payouts."""
#         .format(
#             ratios.get('npm', 0),
#             ratios.get('roa', 0),
#             ratios.get('ocf_lct', 0)
#         )
#     )

# st.markdown("---")
# st.subheader("🔬 Financial Ratios Used in Analysis")
# st.dataframe(st.session_state.input_df.T)

import streamlit as st
import openai

st.title("🤖 GPT-Powered Dividend Interpretation")

# 🔐 Ask user for API key
api_key = st.text_input("🔐 Enter your OpenAI API Key", type="password")
if not api_key:
    st.warning("⚠️ Please enter your OpenAI API key above to continue.")
    st.stop()

openai.api_key = api_key

# ✅ Check if prediction was done earlier
if "prediction_label" not in st.session_state or "input_df" not in st.session_state:
    st.warning("⚠️ Please run a prediction first from the yFinance page.")
    st.stop()

# 🔄 Load values from session state
label = st.session_state.prediction_label
ratios = st.session_state.input_df.iloc[0].to_dict()
ticker = st.session_state.get("ticker", "N/A")
industry = st.session_state.get("industry", "Unknown")

# 🧠 Create GPT prompt
clean_label = label.lower().replace("📈", "increase").replace("📉", "decrease").replace("➖", "stay the same")

prompt = f"""
You are a financial analyst AI. A model predicted that the dividend for ticker {ticker} in the {industry} industry will {clean_label}.
Here are the financial ratios (dictionary format):
{ratios}

Please provide a concise, insightful, and professional analysis explaining the likely reasons behind this dividend change. Highlight the key ratios involved and relate them to the outcome.
"""

# 🤖 Call OpenAI API
with st.spinner("Generating GPT analysis..."):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a financial analyst."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )

        gpt_output = response.choices[0].message["content"]

        # ✅ Display GPT result
        st.markdown("### 📘 GPT Analysis")
        st.write(gpt_output)

    except Exception as e:
        st.error(f"❌ Error during GPT response: {e}")
        st.stop()

# 📊 Show original ratios for reference
st.markdown("---")
st.subheader("📊 Financial Ratios Used")
st.dataframe(st.session_state.input_df.T)
