import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------------------------------------------------------
# 1. PAGE CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Strategic Loan Demand Forecasting",
    page_icon="📈",
    layout="wide"
)

# -----------------------------------------------------------------------------
# 2. HEADER & CONTEXT
# -----------------------------------------------------------------------------
st.title("📈 Strategic Loan Demand Forecasting & Scenario Planning")

st.markdown("""
This dashboard utilizes time-series forecasting to predict future loan demand and 
evaluates the operational impact of changing macroeconomic conditions. Use the sidebar 
to stress-test the economy and observe how lending volume, capital requirements, 
and staffing needs adapt in real-time.
""")
st.divider()

# -----------------------------------------------------------------------------
# 3. SIDEBAR: MACROECONOMIC SCENARIO ENGINE
# -----------------------------------------------------------------------------
st.sidebar.header("Macroeconomic Levers")

# Quick-select scenario buttons
scenario = st.sidebar.radio(
    "Select Economic Scenario:",
    ["Baseline", "Optimistic", "Recession", "Custom Stress Test"]
)

# Define default slider values based on the selected scenario
if scenario == "Optimistic":
    defaults = {"interest": 3.5, "unemployment": 3.0, "inflation": 2.0, "marketing": 115}
elif scenario == "Recession":
    defaults = {"interest": 7.5, "unemployment": 7.0, "inflation": 5.0, "marketing": 90}
else: # Baseline or Custom
    defaults = {"interest": 5.0, "unemployment": 4.0, "inflation": 2.5, "marketing": 100}

# Interactive sliders
interest = st.sidebar.slider("Interest Rate (%)", 1.0, 10.0, defaults["interest"], 0.25)
unemployment = st.sidebar.slider("Unemployment (%)", 2.0, 12.0, defaults["unemployment"], 0.25)
inflation = st.sidebar.slider("Inflation (%)", 0.0, 10.0, defaults["inflation"], 0.1)
marketing = st.sidebar.slider("Marketing Spend Index", 50, 200, defaults["marketing"], 5)

# -----------------------------------------------------------------------------
# 4. SARIMAX MODEL INTEGRATION (FORECASTING)
# -----------------------------------------------------------------------------
import pickle

forecast_horizon = 12

# 1. Load your actual trained model safely
@st.cache_resource
def load_model():
    with open('forecast_model.pkl', 'rb') as f:
        return pickle.load(f)

model = load_model()

# 2. Build the future exogenous dataframe matching your exact 5 exog_cols
future_exog = pd.DataFrame({
    "Interest Rate": [interest] * forecast_horizon,
    "Inflation Rate": [inflation] * forecast_horizon,
    "GDP Growth": [2.0] * forecast_horizon,                # You can leave this as a steady baseline or add a GDP slider if you want!
    "Consumer Confidence": [95.0] * forecast_horizon,      # Baseline estimate for consumer sentiment
    "Marketing Spend": [marketing] * forecast_horizon
})

# 3. Generate predictions from your real fitted_arimax model
forecast = model.get_forecast(steps=forecast_horizon, exog=future_exog)
predicted_apps = forecast.predicted_mean

# Format index as monthly start dates for plotting
months = pd.date_range(start="2026-08-01", periods=forecast_horizon, freq='MS')
predicted_apps.index = months

# Total applications over the next 12 months
total_applications = int(predicted_apps.sum())

# -----------------------------------------------------------------------------
# 5. OPERATIONAL & BUSINESS PLANNING
# -----------------------------------------------------------------------------
# Translating raw application volume into business outcomes
employees_needed = total_applications / 24           # Assumption: 1 officer handles 40 apps/month
capital_required = total_applications * 250000       # Assumption: $250k average loan size
projected_revenue = total_applications * 2500        # Assumption: $2,500 profit per funded loan

st.subheader(f"Executive KPIs: 12-Month Outlook ({scenario})")

# Display top-level metrics
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric("Forecasted Applications", f"{total_applications:,}")
kpi2.metric("Capital Required", f"${capital_required / 1000000:,.1f}M")
kpi3.metric("Projected Revenue", f"${projected_revenue / 1000000:,.2f}M")
kpi4.metric("Est. Loan Officers Needed", f"{round(employees_needed)}")

st.divider()

# -----------------------------------------------------------------------------
# 6. VISUALIZATION
# -----------------------------------------------------------------------------
st.subheader("Application Volume Trajectory")

# Plotting the forecast using Matplotlib
fig, ax = plt.subplots(figsize=(12, 4))
ax.plot(predicted_apps.index, predicted_apps.values, color="#1f77b4", linewidth=2.5, marker='o')

# Formatting the chart for an executive presentation
ax.set_title(f"Predicted Monthly Demand - {scenario} Conditions", fontsize=12)
ax.set_ylabel("Loan Applications")
ax.grid(True, linestyle="--", alpha=0.5)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Render the plot in Streamlit
st.pyplot(fig)