# %%
## Streamlip App Code

# %%
import streamlit as st
import pandas as pd
import joblib

# %%
# Load trained pipeline
pipeline = joblib.load('delay_prediction_pipeline.pkl')

st.set_page_config(page_title="Construction Delay Predictor")
st.title("🏗️ Construction Delay Risk Estimator")

st.markdown("""
Estimate whether a project is likely to be **delayed** based on its early planning details.
""")
st.markdown("### Input Project Details")

# %%
# --- USER INPUT ---
budget = st.number_input("Project Budget ($)", min_value=1000.0, format="%.2f")
duration = st.number_input("Planned Duration (days)", min_value=1)

project_type = st.selectbox("Project Type", [
    'SCA CIP', 'SCA CIP RESOA', 'SCA EmergencyLighting', 'SCA Lease Site Improvement'
])

project_phase = st.selectbox("Project Phase", ['Scope', 'Design', 'Construction', 'CM,F&E'])

start_month = st.selectbox("Project Start Month", [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
])

# %%
# --- ENGINEERED FEATURE ---

budget_per_day = budget / duration

# %%
# --- ASSEMBLE INPUT FOR MODEL ---
input_data = pd.DataFrame([{
    'Budget': budget,
    'Planned_Duration': duration,
    'Budget_Per_Day': budget_per_day,
    'Project Type': project_type,
    'Project Phase Name': project_phase,
    'Project Start_Month': start_month
}])


# %%
# --- PREDICT DELAY ---
if st.button("🧠 Predict Delay Risk"):
    prediction = pipeline.predict(input_data)[0]
    probability = pipeline.predict_proba(input_data)[0][1]

    label = "🚨 Delayed" if prediction == 1 else "✅ On-Time"
    st.subheader(f"Prediction: **{label}**")
    st.write(f"Model confidence in delay: **{probability:.2%}**")

# %%



