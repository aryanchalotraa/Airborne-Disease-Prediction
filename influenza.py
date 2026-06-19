"""
Seasonal Influenza Risk Prediction
---------------------------------
This model predicts MONTHLY INFLUENZA RISK using epidemiological
seasonality patterns.

Reason for rule-based model:
- IDSP influenza data is aggregated and insufficient for
  long-term ML forecasting.
- WHO & CDC recommend seasonality-based risk models
  when longitudinal data is limited.
"""

def predict_influenza(month, temperature, humidity):
    """
    Predicts Influenza Risk Level (Low / Medium / High)

    Scientific basis:
    - Influenza virus survives longer at low temperature
      and moderate to high humidity.
    - Winter season shows peak influenza activity in India.

    Sources:
    WHO: https://www.who.int/teams/global-influenza-programme
    CDC: https://www.cdc.gov/flu/about/season/flu-season.htm
    """

    # Winter months in India
    if month in [11, 12, 1, 2]:
        if temperature < 20 and humidity > 50:
            return "High"
        return "Medium"

    # Monsoon respiratory stress
    if month in [6, 7, 8, 9] and humidity > 70:
        return "Medium"

    return "Low"
