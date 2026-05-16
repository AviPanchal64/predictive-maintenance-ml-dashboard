import streamlit as st


def metric_card(label, value, subtext, colour_class=""):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value {colour_class}">{value}</div>
            <div class="metric-sub">{subtext}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_top_metrics(
    failure_probability,
    health_score,
    risk_level,
    risk_message,
    risk_colour,
    df
):
    normal_count = int((df["Machine failure"] == 0).sum())
    fail_count = int((df["Machine failure"] == 1).sum())

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        metric_card(
            "Failure Probability",
            f"{failure_probability * 100:.2f}%",
            "Predicted probability of machine failure",
            risk_colour
        )

    with col2:
        metric_card(
            "Machine Health Score",
            f"{health_score:.1f}/100",
            "Higher score means healthier machine",
            risk_colour
        )

    with col3:
        metric_card(
            "Risk Level",
            risk_level,
            risk_message,
            risk_colour
        )

    with col4:
        metric_card(
            "Dataset Size",
            f"{len(df):,}",
            f"{fail_count} failures recorded"
        )

    return normal_count, fail_count