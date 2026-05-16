from pathlib import Path

import joblib
import pandas as pd
import streamlit as st


BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_PATH = BASE_DIR / "models" / "failure_prediction_model.joblib"
FEATURES_PATH = BASE_DIR / "models" / "model_features.joblib"
DATA_PATH = BASE_DIR / "data" / "predictive_maintenance.csv"


@st.cache_resource
def load_model():
    model = joblib.load(MODEL_PATH)
    features = joblib.load(FEATURES_PATH)
    return model, features


@st.cache_data
def load_dataset():
    return pd.read_csv(DATA_PATH)