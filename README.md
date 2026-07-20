# Financial Forecasting Dashboard

A comprehensive data analysis and visualization project designed to evaluate historical financial trends and forecast future loan demand. By combining rigorous time series analysis with economic driver evaluation, this dashboard provides executives and financial analysts with actionable insights into business performance, forecasting accuracy, and macroeconomic impacts.

---

## 🎯 Business Objective

The primary goal of this project is to make data-driven decisions using an interactive dashboard built to:

* **Predict** future loan demand accurately.
* **Optimize** resources and capital allocation based on projected needs.
* **Evaluate** the impact of external economic drivers on core business metrics.
* **Support** strategic planning and scenario-based risk management.

---

## 📊 Dashboard Features & Architecture

The dashboard is structured into six key analytical sections, taking the user from a high-level business overview down to granular statistical modeling and future scenario planning.

### 1. Business Overview

A high-level executive summary of financial performance:

* **Key Performance Indicators (KPIs):** Total loan applications, total approved loans, and total loan value generated.
* **Trend Analysis:** Approval rate trends, revenue generated over time, and monthly application volume.
* **Comparative Metrics:** Average loan amounts and year-over-year (YoY) growth in lending activity.

### 2. Time Series Exploration

A deep dive into the historical patterns of the loan application data:

* **Historical Trends:** Visualization of the monthly loan application time series.
* **Seasonality:** Identification of monthly seasonality patterns.
* **Decomposition:** Breakdown of the series into **Trend**, **Seasonal**, and **Residual** components.

### 3. Stationarity Analysis

A transparent view of the statistical preparation required for accurate forecasting:

* **Transformations:** Side-by-side comparison of the original non-stationary series and the first differenced series.
* **Autocorrelation:** Visuals of ACF and PACF plots *before* and *after* differencing to justify model parameters.
* **Statistical Testing:** Display of Augmented Dickey-Fuller (ADF) test results and comparisons of stationarity metrics.

### 4. Forecasting Model Analysis

Evaluation and visualization of predictive model performance:

* **Train/Test Splits:** Clear delineation of training and testing periods.
* **Model Comparison:** Actual vs. Predicted values comparing standard **ARIMA** against **ARIMAX / SARIMAX** models.
* **Forecasts:** Future forecast values complete with confidence intervals.
* **Diagnostics:** Residual analysis and residual autocorrelation checks to ensure model validity.
* **Error Metrics:** Comprehensive accuracy tracking using MAE, RMSE, MAPE, AIC, and BIC.

### 5. Economic Driver Analysis

An investigation into how macroeconomic factors influence financial activity:

* **Variable Comparisons:** Loan application volume analyzed against Interest Rates, Unemployment trends, Inflation rates, and Marketing spend.
* **Macro Impacts:** Analysis of GDP growth impacts on overall lending demand.
* **Correlations:** Correlation heatmaps between economic variables to identify the strongest drivers of loan demand while monitoring for multicollinearity.

### 6. Scenario Planning

Strategic forecasting tools for risk and capital management:

* **Economic Scenarios:** Side-by-side forecasts for Baseline, Optimistic, and Recession scenarios.
* **Stress Testing:** Forecasting loan demand under varying interest rate conditions and unemployment changes.
* **Operational Estimates:** Projections for staffing and capital requirements based on expected application volumes.
* **Business Outcomes:** Comparative analysis of revenue and overall business health under the different assumptions.

---

## 🛠️ Technical Stack & Tools

* **Data Processing & Manipulation:** `pandas`, `numpy`
* **Time Series Modeling:** `statsmodels` (ARIMA, SARIMAX, Seasonal Decomposition, ADF Testing)
* **Evaluation Metrics:** `scikit-learn` (RMSE, MAE)
* **Data Visualization:** `matplotlib`, `seaborn`
* **Dataset:** `financial_forecasting_dataset.csv`

---

## 📂 Repository Structure

```text
Financial_Forecasting/
│
├── data/
│   └── financial_forecasting_dataset.csv
│
├── notebooks/
│   ├── 01_Preprocessing_and_EDA.ipynb
│   └── 02_Forecast_Modeling.ipynb
│
├── app.py                      <-- Interactive Streamlit Dashboard
├── forecast_model.pkl          <-- Exported SARIMAX model object
└── requirements.txt            <-- Python dependencies

```

---

## 🚀 Getting Started

1. **Clone the repository:**
```bash
git clone https://github.com/YourUsername/Financial-Forecasting-Dashboard.git
cd Financial-Forecasting-Dashboard

```

2. **Install dependencies:**
```bash
pip install -r requirements.txt

```

3. **Run the analysis:**
Navigate to the `notebooks/` directory and execute the Jupyter Notebooks sequentially to reproduce the data preparation, modeling, and forecasting steps.
