"""
Seasonal Influenza Risk Prediction Module
Based on epidemiological seasonality patterns (WHO / CDC / IDSP)
"""

def predict_influenza(month, temperature, humidity):
    """
    Predicts monthly influenza risk (Low / Medium / High)
    """

    # Winter months in India
    if month in [11, 12, 1, 2]:
        if temperature < 20 and humidity > 50:
            return "High"
        return "Medium"

    # Monsoon respiratory risk
    if month in [6, 7, 8, 9]:
        if humidity > 70:
            return "Medium"

    return "Low"
