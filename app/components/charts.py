import pandas as pd
import plotly.express as px
import streamlit as st
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split


def render_sensor_and_feature_charts(input_data, model, features):
    left, right = st.columns(2)

    with left:
        st.subheader("Current Sensor Readings")
        st.dataframe(input_data, use_container_width=True)

        sensor_fig = px.bar(
            input_data.T.reset_index(),
            x="index",
            y=0,
            labels={"index": "Sensor", 0: "Value"},
            title="Current Machine Sensor Profile"
        )

        sensor_fig.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(15,23,42,0.4)"
        )

        st.plotly_chart(sensor_fig, use_container_width=True)

    with right:
        st.subheader("Model Feature Importance")

        if hasattr(model, "feature_importances_"):
            importance_df = pd.DataFrame({
                "Feature": features,
                "Importance": model.feature_importances_
            }).sort_values(by="Importance", ascending=True)

            importance_fig = px.bar(
                importance_df,
                x="Importance",
                y="Feature",
                orientation="h",
                title="Most Influential Failure Prediction Features"
            )

            importance_fig.update_layout(
                template="plotly_dark",
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(15,23,42,0.4)"
            )

            st.plotly_chart(importance_fig, use_container_width=True)
        else:
            st.warning("Feature importance is not available for this model.")


def render_dataset_overview(df, normal_count, fail_count):
    st.subheader("Dataset Overview")

    d1, d2, d3 = st.columns(3)

    with d1:
        st.metric("Total Machines", f"{len(df):,}")

    with d2:
        st.metric("Normal Cases", f"{normal_count:,}")

    with d3:
        st.metric("Failure Cases", f"{fail_count:,}")

    failure_counts = df["Machine failure"].value_counts().reset_index()
    failure_counts.columns = ["Machine failure", "Count"]
    failure_counts["Status"] = failure_counts["Machine failure"].map({
        0: "Normal Operation",
        1: "Machine Failure"
    })

    pie_fig = px.pie(
        failure_counts,
        names="Status",
        values="Count",
        title="Failure vs Normal Operation Distribution"
    )

    pie_fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(pie_fig, use_container_width=True)


def render_model_performance(df, model, features):
    st.subheader("Model Performance Summary")

    try:
        X = df[features]
        y = df["Machine failure"]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42,
            stratify=y
        )

        y_pred = model.predict(X_test)

        p1, p2, p3, p4 = st.columns(4)

        with p1:
            st.metric("Accuracy", f"{accuracy_score(y_test, y_pred) * 100:.2f}%")

        with p2:
            st.metric("Precision", f"{precision_score(y_test, y_pred) * 100:.2f}%")

        with p3:
            st.metric("Recall", f"{recall_score(y_test, y_pred) * 100:.2f}%")

        with p4:
            st.metric("F1 Score", f"{f1_score(y_test, y_pred) * 100:.2f}%")

    except Exception as e:
        st.warning("Model performance metrics could not be calculated.")
        st.write(e)