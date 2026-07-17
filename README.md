# Financial_Forecasting

├── data/
│   └── financial_forecasting_dataset.csv   # Raw and processed datasets
├── notebooks/
│   ├── 01_business_overview.ipynb          # EDA and KPI calculations
│   ├── 02_time_series_stationarity.ipynb   # Decomposition, ACF/PACF, ADF tests
│   ├── 03_economic_drivers.ipynb           # Correlation and exogenous variable prep
│   └── 04_forecasting_and_scenarios.ipynb  # ARIMA/SARIMAX modeling and stress testing
├── src/
│   ├── data_cleaning.py                    # Imputation (LOCF) and formatting scripts
│   └── model_evaluation.py                 # Expanding window CV and metric generation
├── dashboard/                              # (Optional) Dashboard application files (e.g., Streamlit/Dash)
├── README.md                               # Project documentation
└── requirements.txt                        # Python dependencies
