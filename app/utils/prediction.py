def get_risk_level(probability):
    if probability < 0.30:
        return "Low Risk", "low", "Machine condition appears stable."
    elif probability < 0.70:
        return "Medium Risk", "medium", "Monitor machine condition and consider preventive maintenance."
    else:
        return "High Risk", "high", "Immediate maintenance inspection is recommended."


def calculate_health_score(probability):
    return max(0, 100 - probability * 100)