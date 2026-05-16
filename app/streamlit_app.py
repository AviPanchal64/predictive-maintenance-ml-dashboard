import pandas as pd
import streamlit as st

from components.charts import (
    render_dataset_overview,
    render_model_performance,
    render_sensor_and_feature_charts,
)
from components.gauges import render_gauge_charts
from components.layout import apply_custom_css, render_footer, render_header
from components.metrics import render_top_metrics
from utils.load_data import load_dataset, load_model
from utils.prediction import calculate_health_score, get_risk_level


st.set_page_config(
    page_title="AI Predictive Maintenance Dashboard",
    page_icon="⚙️",
    layout="wide"
)


model, features = load_model()
df = load_dataset()

apply_custom_css()
render_header()


st.sidebar.title("Machine Sensor Inputs")
st.sidebar.write("Adjust the sensor values to simulate different machine operating conditions.")

air_temp = st.sidebar.slider(
    "Air Temperature [K]",
    float(df["Air temperature [K]"].min()),
    float(df["Air temperature [K]"].max()),
    float(df["Air temperature [K]"].mean())
)

process_temp = st.sidebar.slider(
    "Process Temperature [K]",
    float(df["Process temperature [K]"].min()),
    float(df["Process temperature [K]"].max()),
    float(df["Process temperature [K]"].mean())
)

rot_speed = st.sidebar.slider(
    "Rotational Speed [rpm]",
    int(df["Rotational speed [rpm]"].min()),
    int(df["Rotational speed [rpm]"].max()),
    int(df["Rotational speed [rpm]"].mean())
)

torque = st.sidebar.slider(
    "Torque [Nm]",
    float(df["Torque [Nm]"].min()),
    float(df["Torque [Nm]"].max()),
    float(df["Torque [Nm]"].mean())
)

tool_wear = st.sidebar.slider(
    "Tool Wear [min]",
    int(df["Tool wear [min]"].min()),
    int(df["Tool wear [min]"].max()),
    int(df["Tool wear [min]"].mean())
)


input_data = pd.DataFrame([{
    "Air temperature [K]": air_temp,
    "Process temperature [K]": process_temp,
    "Rotational speed [rpm]": rot_speed,
    "Torque [Nm]": torque,
    "Tool wear [min]": tool_wear
}])


prediction = model.predict(input_data)[0]
failure_probability = model.predict_proba(input_data)[0][1]
health_score = calculate_health_score(failure_probability)

risk_level, risk_colour, risk_message = get_risk_level(failure_probability)


normal_count, fail_count = render_top_metrics(
    failure_probability,
    health_score,
    risk_level,
    risk_message,
    risk_colour,
    df
)

st.markdown("<br>", unsafe_allow_html=True)


if prediction == 1:
    st.error("⚠️ Machine failure risk detected. Maintenance inspection is recommended.")
else:
    st.success("✅ Machine is predicted to operate normally under the current sensor readings.")

st.info(risk_message)


render_gauge_charts(failure_probability, health_score)

render_sensor_and_feature_charts(input_data, model, features)

render_dataset_overview(df, normal_count, fail_count)

render_model_performance(df, model, features)


st.subheader("Maintenance Recommendation")

if failure_probability >= 0.70:
    st.warning(
        """
        High-risk operating condition detected. Immediate inspection is recommended.
        Priority should be given to torque loading, rotational speed stability and tool wear condition.
        """
    )
elif failure_probability >= 0.30:
    st.info(
        """
        Medium-risk condition detected. The machine should remain under monitoring.
        Preventive maintenance should be scheduled if the risk trend increases.
        """
    )
else:
    st.success(
        """
        Low-risk condition detected. The machine appears to be operating within acceptable limits.
        Routine monitoring is recommended.
        """
    )


with st.expander("View Raw Dataset"):
    st.dataframe(df.head(500), use_container_width=True)


render_footer()