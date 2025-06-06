
# import streamlit as st
# import yfinance as yf
# import pandas as pd
# import pickle
# from catboost import CatBoostClassifier
# from xgboost import XGBClassifier
# from lightgbm import LGBMClassifier

# st.title("📈 Predict Dividend Change using yFinance Data")

# ticker_input = st.text_input("Enter a Ticker Symbol (e.g., AAPL, MSFT, GE):", value="AAPL")
# industry = st.selectbox("Select Industry", ["Consumer", "Financials", "Energy", "Other"])
# model_option = st.selectbox("Choose a Model:", ["CatBoost", "XGBoost", "LightGBM"])

# def safe_get(df, key):
#     df = df.T  # transpose to make metrics the columns
#     return df[key].iloc[0] if key in df.columns else 0

# def safe_div(a, b):
#     try:
#         return float(a) / float(b) if a and b and b != 0 else 0
#     except:
#         return 0

# if st.button("🔍 Fetch & Predict"):
#     try:
#         stock = yf.Ticker(ticker_input)
#         # Retrieve quarterly statements
#         income_raw = stock.quarterly_income_stmt
#         balance_raw = stock.quarterly_balance_sheet
#         cashflow_raw = stock.quarterly_cashflow

#         st.write("🧾 Income Statement Shape:", income_raw.shape)
#         st.write("🧾 Balance Sheet Shape:", balance_raw.shape)
#         st.write("🧾 Cash Flow Shape:", cashflow_raw.shape)

#         if income_raw.empty or balance_raw.empty or cashflow_raw.empty:
#             st.error("❌ One or more financial statements are unavailable. Try a different ticker.")
#             st.stop()

#         # Compute total debt
#         short_debt = safe_get(balance_raw, "Short Long Term Debt")
#         long_debt = safe_get(balance_raw, "Long Term Debt")
#         total_debt = short_debt + long_debt

#         # Compute ratios
#         ratios = {
#             'dpr': safe_div(safe_get(cashflow_raw, "Cash Dividends Paid"), safe_get(income_raw, "Net Income")),
#             'roe': safe_div(safe_get(income_raw, "Net Income"), safe_get(balance_raw, "Stockholders Equity")),
#             'roa': safe_div(safe_get(income_raw, "Net Income"), safe_get(balance_raw, "Total Assets")),
#             'GProf': safe_div(safe_get(income_raw, "Gross Profit"), safe_get(income_raw, "Total Revenue")),
#             'npm': safe_div(safe_get(income_raw, "Net Income"), safe_get(income_raw, "Total Revenue")),
#             'fcf_ocf': safe_div(safe_get(cashflow_raw, "Free Cash Flow"), safe_get(cashflow_raw, "Operating Cash Flow")),
#             'cash_debt': safe_div(safe_get(balance_raw, "Cash And Cash Equivalents"), total_debt),
#             'cash_lt': safe_div(safe_get(balance_raw, "Cash And Cash Equivalents"), long_debt),
#             'ocf_lct': safe_div(safe_get(cashflow_raw, "Operating Cash Flow"), total_debt),
#             'totdebt_invcap': safe_div(total_debt, safe_get(balance_raw, "Invested Capital")),
#             'de_ratio': safe_div(total_debt, safe_get(balance_raw, "Stockholders Equity")),
#             'debt_ebitda': safe_div(total_debt, safe_get(income_raw, "EBITDA")),
#             'intcov_ratio': safe_div(safe_get(income_raw, "EBIT"), safe_get(income_raw, "Interest Expense")),
#             'curr_ratio': safe_div(safe_get(balance_raw, "Current Assets"), safe_get(balance_raw, "Current Liabilities")),
#             'cash_ratio': safe_div(safe_get(balance_raw, "Cash And Cash Equivalents"), safe_get(balance_raw, "Current Liabilities")),
#             'quick_ratio': safe_div(safe_get(balance_raw, "Current Assets") - safe_get(balance_raw, "Inventory"), safe_get(balance_raw, "Current Liabilities")),
#         }

#         input_df = pd.DataFrame([ratios])
#         input_df.fillna(0, inplace=True)
#         if input_df.isnull().values.any():
#             st.warning("⚠️ Warning: NaN detected in input. Filling with 0.")

#         st.subheader("📋 Computed Financial Ratios")
#         st.dataframe(input_df.T)

#         # Model path logic
#         sector_key = industry.lower()
#         model_paths = {
#             "CatBoost": f"models/catboost_model_{sector_key}.pkl",
#             "XGBoost": f"models/xgboost_model_{sector_key}.pkl",
#             "LightGBM": f"models/lightgbm_model_{sector_key}.pkl",
#         }
#         model_path = model_paths[model_option]

#         with open(model_path, "rb") as f:
#             model = pickle.load(f)

#                 # Prediction and probabilities
#         y_pred = model.predict(input_df)
#         y_proba = model.predict_proba(input_df)[0]

#         label_map = {
#              -1: "📉 Decrease",
#              0: "➖ No Change",
#              1: "📈 Increase"
#         }
#   # Display prediction
#         pred = int(y_pred.flatten()[0]) if hasattr(y_pred, 'flatten') else int(y_pred[0])
#         st.success(f"📊 Predicted Dividend Change: *{label_map[pred]}*")

#         # Show probabilities as chart
#         proba_map = {-1: y_proba[-1], 0: y_proba[0], 1: y_proba[1]}
#         proba_df = pd.DataFrame.from_dict(
#             {label_map[k]: [v] for k, v in proba_map.items()},
#             orient='columns'
#         )
#         st.subheader("🔢 Prediction Probabilities")
#         st.bar_chart(proba_df.T.rename(columns={0: "Probability"}))

#     except Exception as e:
#         st.error(f"❌ Error during prediction: {e}")




#     except Exception as e:
#         st.error(f"❌ Error during prediction: {e}")

import streamlit as st
import yfinance as yf
import pandas as pd
import pickle
from catboost import CatBoostClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier

st.title("📈 Predict Dividend Change using yFinance Data")

ticker_input = st.text_input("Enter a Ticker Symbol (e.g., AAPL, MSFT, GE):", value="AAPL")
industry = st.selectbox("Select Industry", ["Consumer", "Financials", "Energy", "Other"])
model_option = st.selectbox("Choose a Model:", ["CatBoost", "XGBoost", "LightGBM"])

def safe_get(df, key):
    df = df.T
    return df[key].iloc[0] if key in df.columns else 0

def safe_div(a, b):
    try:
        return float(a) / float(b) if a and b and b != 0 else 0
    except:
        return 0

if st.button("🔍 Fetch & Predict"):
    try:
        stock = yf.Ticker(ticker_input)
        income_raw = stock.quarterly_income_stmt
        balance_raw = stock.quarterly_balance_sheet
        cashflow_raw = stock.quarterly_cashflow

        st.write("🧾 Income Statement Shape:", income_raw.shape)
        st.write("🧾 Balance Sheet Shape:", balance_raw.shape)
        st.write("🧾 Cash Flow Shape:", cashflow_raw.shape)

        if income_raw.empty or balance_raw.empty or cashflow_raw.empty:
            st.error("❌ One or more financial statements are unavailable. Try a different ticker.")
            st.stop()

        short_debt = safe_get(balance_raw, "Short Long Term Debt")
        long_debt = safe_get(balance_raw, "Long Term Debt")
        total_debt = short_debt + long_debt

        ratios = {
            'dpr': safe_div(safe_get(cashflow_raw, "Cash Dividends Paid"), safe_get(income_raw, "Net Income")),
            'roe': safe_div(safe_get(income_raw, "Net Income"), safe_get(balance_raw, "Stockholders Equity")),
            'roa': safe_div(safe_get(income_raw, "Net Income"), safe_get(balance_raw, "Total Assets")),
            'GProf': safe_div(safe_get(income_raw, "Gross Profit"), safe_get(income_raw, "Total Revenue")),
            'npm': safe_div(safe_get(income_raw, "Net Income"), safe_get(income_raw, "Total Revenue")),
            'fcf_ocf': safe_div(safe_get(cashflow_raw, "Free Cash Flow"), safe_get(cashflow_raw, "Operating Cash Flow")),
            'cash_debt': safe_div(safe_get(balance_raw, "Cash And Cash Equivalents"), total_debt),
            'cash_lt': safe_div(safe_get(balance_raw, "Cash And Cash Equivalents"), long_debt),
            'ocf_lct': safe_div(safe_get(cashflow_raw, "Operating Cash Flow"), total_debt),
            'totdebt_invcap': safe_div(total_debt, safe_get(balance_raw, "Invested Capital")),
            'de_ratio': safe_div(total_debt, safe_get(balance_raw, "Stockholders Equity")),
            'debt_ebitda': safe_div(total_debt, safe_get(income_raw, "EBITDA")),
            'intcov_ratio': safe_div(safe_get(income_raw, "EBIT"), safe_get(income_raw, "Interest Expense")),
            'curr_ratio': safe_div(safe_get(balance_raw, "Current Assets"), safe_get(balance_raw, "Current Liabilities")),
            'cash_ratio': safe_div(safe_get(balance_raw, "Cash And Cash Equivalents"), safe_get(balance_raw, "Current Liabilities")),
            'quick_ratio': safe_div(safe_get(balance_raw, "Current Assets") - safe_get(balance_raw, "Inventory"), safe_get(balance_raw, "Current Liabilities")),
        }

        input_df = pd.DataFrame([ratios])
        input_df.fillna(0, inplace=True)
        if input_df.isnull().values.any():
            st.warning("⚠️ Warning: NaN detected in input. Filling with 0.")

        st.subheader("📋 Computed Financial Ratios")
        st.dataframe(input_df.T)

        # Model loading and prediction
        sector_key = industry.lower()
        model_paths = {
            "CatBoost": f"models/catboost_model_{sector_key}.pkl",
            "XGBoost": f"models/xgboost_model_{sector_key}.pkl",
            "LightGBM": f"models/lightgbm_model_{sector_key}.pkl",
        }

        model_path = model_paths[model_option]
        with open(model_path, "rb") as f:
            model = pickle.load(f)

        # Prediction and probabilities
        y_pred = model.predict(input_df)
        y_proba = model.predict_proba(input_df)[0]

        label_map = {
             -1: "📉 Decrease",
             0: "➖ No Change",
             1: "📈 Increase"
        }
        # Display prediction
        pred = int(y_pred.flatten()[0]) if hasattr(y_pred, 'flatten') else int(y_pred[0])
        st.success(f"📊 Predicted Dividend Change: *{label_map[pred]}*")

        # Show probabilities as chart
        proba_map = {-1: y_proba[-1], 0: y_proba[0], 1: y_proba[1]}
        proba_df = pd.DataFrame.from_dict(
            {label_map[k]: [v] for k, v in proba_map.items()},
            orient='columns'
        )
        st.subheader("🔢 Prediction Probabilities")
        st.bar_chart(proba_df.T.rename(columns={0: "Probability"}))

        st.session_state.prediction_label = label_map[pred]
        st.session_state.input_df = input_df
        st.session_state.ticker = ticker_input
        st.session_state.industry = industry


        # 🧠 Heuristic GPT-style interpretation
        st.markdown("---")
        st.title("GPT-Style Analysis of Dividend Prediction")

        label = label_map[pred]
        st.markdown(f"### Ticker: `{ticker_input}` | Industry: `{industry}`")
        st.markdown(f"### 📊 Predicted Dividend Change: **{label}**")

        if label == "📈 Increase":
            st.success(
                """The model expects a dividend **increase**. This is likely supported by high profitability indicators such as:
- Return on Equity (ROE): {:.2f}  
- Net Profit Margin (NPM): {:.2f}  
- Free Cash Flow / Operating Cash Flow: {:.2f}

Additionally, liquidity metrics like the Quick Ratio ({:.2f}) and Cash Ratio ({:.2f}) suggest the company is well-positioned to distribute earnings."""
                .format(
                    ratios.get('roe', 0),
                    ratios.get('npm', 0),
                    ratios.get('fcf_ocf', 0),
                    ratios.get('quick_ratio', 0),
                    ratios.get('cash_ratio', 0)
                )
            )
        elif label == "📉 Decrease":
            st.warning(
                """The model forecasts a **decrease** in dividends. Possible contributing factors:
- Interest Coverage Ratio: {:.2f}  
- Debt/EBITDA: {:.2f}  
- Debt-to-Equity Ratio: {:.2f}  
- Weak Profitability (ROE: {:.2f}, NPM: {:.2f})

These suggest financial strain or a conservative capital structure."""
                .format(
                    ratios.get('intcov_ratio', 0),
                    ratios.get('debt_ebitda', 0),
                    ratios.get('de_ratio', 0),
                    ratios.get('roe', 0),
                    ratios.get('npm', 0)
                )
            )
        else:
            st.info(
                """The dividend is expected to remain **unchanged**. This likely reflects a stable but conservative financial position:
- Net Profit Margin: {:.2f}  
- Return on Assets: {:.2f}  
- Operating Cash Flow to Long-Term Debt: {:.2f}

These indicators support maintaining, rather than increasing or decreasing, dividend payouts."""
                .format(
                    ratios.get('npm', 0),
                    ratios.get('roa', 0),
                    ratios.get('ocf_lct', 0)
                )
            )

    except Exception as e:
        st.error(f"❌ Error during prediction: {e}")

