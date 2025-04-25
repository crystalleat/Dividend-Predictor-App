import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("🏠 About our Dataset")

st.subheader(" Access our Colab notebook here : https://colab.research.google.com/drive/1Ocjx5k9_szTnyFYZKBLshATQ1fFTpbeV?usp=sharing")
# --- Load training dataset ---
try:
    df = pd.read_csv("data/dividends.csv")
    st.success("✅ Training data loaded from `data/dividends.csv`")
except Exception as e:
    st.error(f"❌ Could not load training data: {e}")
    st.stop()

# --- Dataset preview ---
with st.expander("📋 Preview Dataset"):
    st.dataframe(df.head(20), use_container_width=True)

# --- Summary statistics ---
with st.expander("📊 Summary Statistics"):
    st.write(df.describe().T.round(2))

# --- Sidebar filter ---
st.sidebar.header("🔎 Filter by Ticker and Metric")
ticker = st.sidebar.selectbox("Select Ticker:", sorted(df["TICKER"].unique()))
metric = st.sidebar.selectbox("Select Financial Metric:", [
    'dpr', 'roe', 'roa', 'GProf', 'npm', 'fcf_ocf', 'cash_debt',
    'cash_lt', 'ocf_lct', 'totdebt_invcap', 'de_ratio',
    'debt_ebitda', 'intcov_ratio', 'curr_ratio',
    'cash_ratio', 'quick_ratio'
])

# --- Plot selected metric ---
filtered = df[df["TICKER"] == ticker].sort_values("qtr_yr")
st.subheader(f"📈 {metric.upper()} for {ticker} Over Time")

fig, ax = plt.subplots(figsize=(10, 4))
sns.lineplot(data=filtered, x="qtr_yr", y=metric, marker="o", ax=ax)
plt.xticks(rotation=45)
plt.title(f"{ticker} - {metric.upper()} by Quarter")
plt.tight_layout()
st.pyplot(fig)

# --- Download filtered data ---
st.download_button(
    label="📥 Download Filtered Data",
    data=filtered.to_csv(index=False),
    file_name=f"{ticker}_{metric}_history.csv",
    mime="text/csv"
)
