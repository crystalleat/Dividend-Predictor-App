# Dividend Trend Prediction App

This Streamlit web application predicts whether a public company's dividend payout is likely to **increase**, **decrease**, or **stay the same** based on financial ratio analysis. The model leverages historical financial data and live updates from `yfinance` to generate real-time predictions for multiple industries.


## Features

- **Real-Time Dividend Prediction** using latest quarterly financials
- **Industry-Specific Models**: Financials, Consumer, Energy, and Others
- **Interactive Visuals**: Classification reports, confusion matrices, probability scores
- **Built-in Financial Ratio Calculator** for all key metrics
- **Model Training Code Access** with rationale and performance details


## Models Used

| Model    | Strengths |
|----------|-----------|
| CatBoost | Handles imbalanced datasets, robust for smaller tabular data |
| LightGBM + Voting Ensemble | Fast, memory-efficient; combined with Logistic Regression and Decision Tree |
| XGBoost  | High performance with strong regularization and feature handling |


## Financial Ratios Used

The model uses 16+ key financial ratios across:

- **Profitability**: ROE, ROA, Net Profit Margin, Gross Profit
- **Liquidity**: Current Ratio, Quick Ratio, Cash Ratio
- **Leverage**: D/E, Debt/EBITDA, Interest Coverage
- **Cash Flow**: FCF/OCF, OCF/LTD
- **Dividend Target**: DPR (Dividend Payout Ratio)


## Tech Stack

- `streamlit` for frontend UI
- `yfinance` for real-time data access
- `pandas`, `matplotlib`, `seaborn` for data processing and visualizations
- `scikit-learn`, `xgboost`, `catboost`, `lightgbm` for modeling
- `openai` for GPT-powered natural language explanation


## Data Sources

- **Training Data**: WRDS / CRSP dataset (20 years of dividend and ratio history)
- **Live Testing**: Pulled dynamically from `yfinance` for any ticker


## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/akshara2403/Dividend-Predictor-App.git
cd Dividend-Predictor-App
```

2. Install Requirements
Ensure Python 3.10 is installed, then:

```bash 
pip install -r requirements.txt
```
3. Run the App
```bash
streamlit run app.py
```



Folder Structure
```bash
.
├── app.py                    # Main entry point with multi-page navigation
├── pages/                   # All Streamlit subpages
│   ├── about.py             # About project
│   ├── code.py              # Model training code (tabbed)
│   ├── main.py              # Our dataset
│   ├── Ratios_we_used.py    # Look into the ratios used for our dataset
│   └── predict_from_yfinance.py

├── models/                  # Trained .pkl files per industry
├── images/                  # Confusion matrices and reports
├── data/                    # Optional CSVs or cache
├── requirements.txt
└── README.md
```
Team Members:

- Akshara Ramprasad – MSDS 2025

- Samritha Aadhi Ravikumar – MSDS 2025

- Crystal Leatvanich – MSBA 2025

Future Work

- Expand model to include more sectors and global tickers

- Improve class imbalance handling using smarter sampling

- Add model drift monitoring and alerts

License

- None. Feel free to use and modify with credit.

Created as part of BA870 Financial Analytics @ Boston University
