"""
Disease Risk Logic Module
-------------------------
This module predicts CLIMATE-DRIVEN HEALTH RISKS (not diagnosis).

All thresholds used below are derived from established public health
guidelines and peer-reviewed research published by WHO, CDC, CPCB,
NDMA, and MoHFW.

The system predicts population-level RISK, not individual disease.
"""

def predict_diseases(pm25, pm10, aqi, temp, humidity, month):
    risks = []

    # =====================================================
    # AIR POLLUTION → RESPIRATORY DISEASE RISK
    # =====================================================
    # Scientific basis:
    # - WHO Air Quality Guidelines (2021)
    # - CPCB National AQI Standards (India)
    #
    # Evidence:
    # PM2.5 > 150 µg/m³ significantly increases asthma, COPD,
    # bronchitis, and other respiratory morbidity.
    #
    # Sources:
    # WHO: https://www.who.int/publications/i/item/9789240034228
    # CPCB AQI: https://cpcb.nic.in/National-Air-Quality-Index/

    if pm25 > 150 or aqi >= 4:
        risks.append("Asthma / COPD Risk")

    if pm10 > 150:
        risks.append("Bronchitis Risk")

    if pm25 > 80:
        risks.append("Allergic Respiratory Infection Risk")

    # =====================================================
    # SEASONAL INFLUENZA (AIRBORNE VIRAL DISEASE)
    # =====================================================
    # Scientific basis:
    # - WHO Influenza Seasonality Reports
    # - CDC Influenza Transmission Studies
    # - ICMR Seasonal Influenza Surveillance
    #
    # Evidence:
    # Influenza transmission increases in winter months
    # when temperature < 20°C and relative humidity > 50%.
    #
    # Sources:
    # WHO: https://www.who.int/teams/global-influenza-programme
    # CDC: https://www.cdc.gov/flu/about/season/flu-season.htm
    # ICMR: https://main.icmr.nic.in/

    if month in [11, 12, 1, 2] and temp < 20 and humidity > 50:
        risks.append("Seasonal Influenza Risk")

    # =====================================================
    # HEAT-RELATED ILLNESS (CLIMATE STRESS)
    # =====================================================
    # Scientific basis:
    # - WHO Heat-Health Action Plans
    # - NDMA Heatwave Guidelines (India)
    # - IMD Heatwave Criteria
    #
    # Evidence:
    # Temperatures ≥ 40°C increase risk of heat exhaustion,
    # heat stroke, and dehydration.
    #
    # Sources:
    # WHO: https://www.who.int/publications/i/item/WHO-WHE-EPE-17.1
    # NDMA: https://ndma.gov.in/Natural-Hazards/Heat-Wave
    # IMD: https://mausam.imd.gov.in/

    if temp >= 40:
        risks.append("Heat Exhaustion / Heat Stroke Risk")

    if temp >= 38 and humidity < 40:
        risks.append("Dehydration Risk")

    # =====================================================
    # MONSOON / HIGH HUMIDITY → SKIN & WATER-RELATED INFECTIONS
    # =====================================================
    # Scientific basis:
    # - MoHFW Monsoon Advisory
    # - WHO Water-borne Disease Reports
    # - IDSP Seasonal Outbreak Analysis
    #
    # Evidence:
    # High humidity (>80%) creates favorable conditions
    # for fungal skin infections and water contamination.
    #
    # Sources:
    # MoHFW: https://www.mohfw.gov.in/
    # WHO Water Safety: https://www.who.int/teams/environment-climate-change-and-health/water-sanitation-and-health

    if humidity >= 80:
        risks.append("Skin Infection Risk")

    return list(set(risks))
