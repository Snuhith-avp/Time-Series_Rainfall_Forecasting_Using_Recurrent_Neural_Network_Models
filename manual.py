import streamlit as st
import pandas as pd
import predict

def manual():
    st.markdown(
        """
        <style>
            body {
                background-color: #87CEEB;
                font-family: 'Arial', sans-serif;
            }
            .header {
                color: #ffffff;
                font-size: 3em;
                padding: 20px;
                text-align: center;
                font-weight: bold;
            }
            .description {
                color: #ffffff;
                font-size: 1.5em;
                padding: 20px;
                text-align: center;
            }
            .usage {
                color: #1f4e79;
                font-size: 2em;
                font-weight: bold;
                padding: 10px;
            }
            .button {
                background-color: #1f4e79;
                color: white;
                font-size: 1.5em;
                padding: 15px 30px;
                border-radius: 8px;
                margin-top: 20px;
                cursor: pointer;
                transition: background-color 0.3s;
            }
            .button:hover {
                background-color: #15335e;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div class='header'>Rainfall Prediction App</div>", unsafe_allow_html=True)
    st.markdown("<div class='description'>Predict rainfall based on weather conditions.</div>", unsafe_allow_html=True)

    TempHighF = st.slider("Temperature High (F)", min_value=0, max_value=100, value=50)
    TempAvgF = st.slider("Temperature Avg (F)", min_value=0, max_value=100, value=25)
    TempLowF = st.slider("Temperature Low (F)", min_value=0, max_value=100, value=10)
    DewPointHighF = st.slider("Dew Point High (F)", min_value=0, max_value=100, value=30)
    DewPointAvgF = st.slider("Dew Point Avg (F)", min_value=0, max_value=100, value=15)
    DewPointLowF = st.slider("Dew Point Low (F)", min_value=0, max_value=100, value=5)
    HumidityHighPercent = st.slider("Humidity High (%)", min_value=0, max_value=100, value=80)
    HumidityAvgPercent = st.slider("Humidity Avg (%)", min_value=0, max_value=100, value=50)
    HumidityLowPercent = st.slider("Humidity Low (%)", min_value=0, max_value=100, value=20)
    SeaLevelPressureHighInches = st.slider("Sea Level Pressure High (inches)", min_value=28, max_value=31, value=30)
    SeaLevelPressureAvgInches = st.slider("Sea Level Pressure Avg (inches)", min_value=28, max_value=31, value=29)
    SeaLevelPressureLowInches = st.slider("Sea Level Pressure Low (inches)", min_value=28, max_value=31, value=28)
    VisibilityHighMiles = st.slider("Visibility High (Miles)", min_value=0, max_value=10, value=8)
    VisibilityAvgMiles = st.slider("Visibility Avg (Miles)", min_value=0, max_value=10, value=5)
    VisibilityLowMiles = st.slider("Visibility Low (Miles)", min_value=0, max_value=10, value=2)
    WindHighMPH = st.slider("Wind High (MPH)", min_value=0, max_value=50, value=20)
    WindAvgMPH = st.slider("Wind Avg (MPH)", min_value=0, max_value=50, value=10)
    WindGustMPH = st.slider("Wind Gust (MPH)", min_value=0, max_value=50, value=15)

    events_options = ["Rain", "Snow", "Thunderstorm", "Wind", "Fog"]
    selected_events = st.multiselect("Select Events", events_options)

    day = st.slider("Day", min_value=1, max_value=31, value=15)
    month = st.slider("Month", min_value=1, max_value=12, value=6)
    year = st.slider("Year", min_value=2000, max_value=2024, value=2022)

    if st.button("Predict Rainfall"):
        data = {
            'TempHighF': TempHighF, 'TempAvgF': TempAvgF, 'TempLowF': TempLowF,
            'DewPointHighF': DewPointHighF, 'DewPointAvgF': DewPointAvgF, 'DewPointLowF': DewPointLowF,
            'HumidityHighPercent': HumidityHighPercent, 'HumidityAvgPercent': HumidityAvgPercent, 'HumidityLowPercent': HumidityLowPercent,
            'SeaLevelPressureHighInches': SeaLevelPressureHighInches, 'SeaLevelPressureAvgInches': SeaLevelPressureAvgInches, 'SeaLevelPressureLowInches': SeaLevelPressureLowInches,
            'VisibilityHighMiles': VisibilityHighMiles, 'VisibilityAvgMiles': VisibilityAvgMiles, 'VisibilityLowMiles': VisibilityLowMiles,
            'WindHighMPH': WindHighMPH, 'WindAvgMPH': WindAvgMPH, 'WindGustMPH': WindGustMPH, 'Events': selected_events,
            'Day': day, 'Year': year, 'Month': month
        }

        features_df = pd.DataFrame([data])

        features_df['Events'] = features_df['Events'].apply(lambda x: ','.join(x) if isinstance(x, list) else x)
        predicted_rainfall = predict.predict_rainfall(features_df)

        st.success(f"Predicted Rainfall: {predicted_rainfall[0]:.2f} inches")
