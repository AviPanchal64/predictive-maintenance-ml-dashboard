import plotly.graph_objects as go
import streamlit as st


def render_gauge_charts(failure_probability, health_score):
    g1, g2 = st.columns(2)

    with g1:
        fig_prob = go.Figure(go.Indicator(
            mode="gauge+number",
            value=failure_probability * 100,
            title={"text": "Failure Probability (%)"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#ef4444"},
                "steps": [
                    {"range": [0, 30], "color": "rgba(34,197,94,0.35)"},
                    {"range": [30, 70], "color": "rgba(245,158,11,0.35)"},
                    {"range": [70, 100], "color": "rgba(239,68,68,0.35)"}
                ],
            }
        ))

        fig_prob.update_layout(
            height=350,
            paper_bgcolor="rgba(0,0,0,0)",
            font={"color": "#f8fafc"}
        )

        st.plotly_chart(fig_prob, use_container_width=True)

    with g2:
        fig_health = go.Figure(go.Indicator(
            mode="gauge+number",
            value=health_score,
            title={"text": "Machine Health Score"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#22c55e"},
                "steps": [
                    {"range": [0, 30], "color": "rgba(239,68,68,0.35)"},
                    {"range": [30, 70], "color": "rgba(245,158,11,0.35)"},
                    {"range": [70, 100], "color": "rgba(34,197,94,0.35)"}
                ],
            }
        ))

        fig_health.update_layout(
            height=350,
            paper_bgcolor="rgba(0,0,0,0)",
            font={"color": "#f8fafc"}
        )

        st.plotly_chart(fig_health, use_container_width=True)