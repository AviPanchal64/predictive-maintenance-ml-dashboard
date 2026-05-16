import streamlit as st


def apply_custom_css():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(135deg, #07111f 0%, #0f172a 45%, #020617 100%);
            color: #e5e7eb;
        }

        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #020617 0%, #0f172a 100%);
            border-right: 1px solid rgba(148, 163, 184, 0.2);
        }

        h1, h2, h3 {
            color: #f8fafc;
        }

        .main-title {
            font-size: 42px;
            font-weight: 800;
            color: #f8fafc;
            margin-bottom: 5px;
        }

        .subtitle {
            font-size: 17px;
            color: #94a3b8;
            margin-bottom: 25px;
        }

        .metric-card {
            background: rgba(15, 23, 42, 0.85);
            border: 1px solid rgba(148, 163, 184, 0.2);
            border-radius: 18px;
            padding: 22px;
            box-shadow: 0 12px 35px rgba(0,0,0,0.35);
        }

        .metric-label {
            color: #94a3b8;
            font-size: 14px;
            font-weight: 600;
            text-transform: uppercase;
        }

        .metric-value {
            color: #f8fafc;
            font-size: 32px;
            font-weight: 800;
            margin-top: 8px;
        }

        .metric-sub {
            color: #94a3b8;
            font-size: 13px;
            margin-top: 6px;
        }

        .low {
            color: #22c55e;
        }

        .medium {
            color: #f59e0b;
        }

        .high {
            color: #ef4444;
        }

        .footer {
            text-align: center;
            color: #94a3b8;
            padding: 25px;
            font-size: 14px;
        }

        div[data-testid="stMetric"] {
            background: rgba(15, 23, 42, 0.8);
            border: 1px solid rgba(148, 163, 184, 0.2);
            padding: 18px;
            border-radius: 16px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


def render_header():
    st.markdown(
        """
        <div class="main-title">⚙️ AI Predictive Maintenance Dashboard</div>
        <div class="subtitle">
            Machine learning platform for predicting industrial equipment failure using real sensor data.
        </div>
        """,
        unsafe_allow_html=True
    )


def render_footer():
    st.markdown("---")
    st.markdown(
        """
        <div class="footer">
            Developed by <b>Avi Panchal</b> · AI Predictive Maintenance & Industrial Analytics Platform
        </div>
        """,
        unsafe_allow_html=True
    )