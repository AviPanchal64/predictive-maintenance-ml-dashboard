import joblib
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(
    page_title="AI Predictive Maintenance Dashboard",
    page_icon="⚙️",
    layout="wide"
)

# Load trained model and feature list
model = joblib.load("models/failure_prediction_model.joblib")
features = joblib.load("models/model_features.joblib")

st.title("⚙️ AI Predictive Maintenance Dashboard")

st.write(
    """
    This dashboard predicts the probability of industrial machine failure
    using sensor data such as temperature, rotational speed, torque and tool wear.
    """
)

# Sidebar inputs
st.sidebar.header("Machine Sensor Inputs")

air_temp = st.sidebar.slider(
    "Air Temperature [K]",
    min_value=295.0,
    max_value=305.0,
    value=300.0
)

process_temp = st.sidebar.slider(
    "Process Temperature [K]",
    min_value=305.0,
    max_value=315.0,
    value=310.0
)

rot_speed = st.sidebar.slider(
    "Rotational Speed [rpm]",
    min_value=1000,
    max_value=3000,
    value=1500
)

torque = st.sidebar.slider(
    "Torque [Nm]",
    min_value=0.0,
    max_value=80.0,
    value=40.0
)

tool_wear = st.sidebar.slider(
    "Tool Wear [min]",
    min_value=0,
    max_value=250,
    value=100
)

# Put inputs into dataframe
input_data = pd.DataFrame([{
    "Air temperature [K]": air_temp,
    "Process temperature [K]": process_temp,
    "Rotational speed [rpm]": rot_speed,
    "Torque [Nm]": torque,
    "Tool wear [min]": tool_wear
}])

# Prediction
prediction = model.predict(input_data)[0]
failure_probability = model.predict_proba(input_data)[0][1]
health_score = 100 - (failure_probability * 100)

# Risk level
if failure_probability < 0.30:
    risk_level = "Low Risk"
    risk_message = "Machine condition appears stable."
elif failure_probability < 0.70:
    risk_level = "Medium Risk"
    risk_message = "Monitor machine condition and consider preventive maintenance."
else:
    risk_level = "High Risk"
    risk_message = "Immediate maintenance inspection is recommended."

# Top metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Failure Probability", f"{failure_probability * 100:.2f}%")

with col2:
    st.metric("Machine Health Score", f"{health_score:.1f}/100")

with col3:
    st.metric("Risk Level", risk_level)

# Prediction result
st.subheader("Prediction Result")

if prediction == 1:
    st.error("⚠️ Machine failure risk detected.")
else:
    st.success("✅ Machine is predicted to operate normally.")

st.info(risk_message)

# Input table
st.subheader("Current Sensor Readings")
st.dataframe(input_data, use_container_width=True)

# Sensor chart
st.subheader("Sensor Profile")

fig = go.Figure()

fig.add_trace(go.Bar(
    x=input_data.columns,
    y=input_data.iloc[0].values
))

fig.update_layout(
    title="Current Machine Sensor Readings",
    xaxis_title="Sensor",
    yaxis_title="Value",
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)

# Maintenance recommendation
st.subheader("Maintenance Recommendation")

if failure_probability >= 0.70:
    st.warning(
        "High risk detected. Inspect torque, rotational speed and tool wear urgently."
    )
elif failure_probability >= 0.30:
    st.info(
        "Medium risk detected. Continue monitoring and schedule preventive maintenance if the risk increases."
    )
else:
    st.success(
        "Low risk detected. Machine conditions appear acceptable."
    )

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align:center; color:gray; padding:15px;'>
        Developed by <b>Avi Panchal</b> · AI Predictive Maintenance Dashboard
    </div>
    """,
    unsafe_allow_html=True
)