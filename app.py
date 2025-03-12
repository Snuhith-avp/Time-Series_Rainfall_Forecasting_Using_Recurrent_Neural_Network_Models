import streamlit as st
from datetime import datetime, timedelta
import calculations
import manual, about_me, predict
import header_footer
import random

# Custom CSS for background image
def add_bg_from_url(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Function to simulate rainfall prediction for the next 7 days (Data basis)
def generate_rainfall_predictions(start_date, num_days=7):
    rainfall_predictions = {}
    for i in range(num_days):
        forecast_date = start_date + timedelta(days=i)
        # Generate a random rainfall prediction (just for demo purposes)
        rainfall_predictions[forecast_date.strftime("%Y-%m-%d")] = round(random.uniform(0, 3), 2)  # rainfall in inches
    return rainfall_predictions

# Main function
def main():

    add_bg_from_url("https://images.unsplash.com/photo-1519692933481-e162a57d6721?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8cmFpbnxlbnwwfHwwfHx8MA%3D%3D")
    
    # Create a sidebar navigation bar
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select a page", ["Home", "Manual Usage", "About Us"])
    
    # Show different content based on the selected page
    if page == "Home":
        # Rest of your app logic
        st.title("Rainfall Forecasting using RNN and  Data basis")
        header_footer.create_header()
        
        current_date = datetime.now().date()
        selected_date = st.date_input("Select a starting date for the forecast", current_date)

        # Fetching RNN predictions (for the selected date)
        forecast_start_date = selected_date
        forecast_end_date = selected_date + timedelta(days=5)  # Example 5-day forecast for RNN
        
        if forecast_start_date <= selected_date <= forecast_end_date:
            selected_date_str = selected_date.strftime("%Y-%m-%d")
            
            try:
                # Fetch input data using calculations.getData
                inputs = calculations.getData(selected_date_str)
                st.write(f"Inputs (from calculations.getData): {inputs}")  # Debugging the inputs to verify data
                
                # Check if the inputs are a dictionary
                if not isinstance(inputs, dict):
                    st.error(f"Expected a dictionary from calculations.getData, but got {type(inputs)}. Data: {inputs}")
                    return

                # Predict rainfall using the fetched inputs
                predicted_rainfall = predict.predict_rainfall(inputs)
                st.write(f"Predicted Rainfall (from predict.predict_rainfall): {predicted_rainfall}")  # Debugging the prediction
                
                # Check if predicted_rainfall is a list and has values
                if isinstance(predicted_rainfall, list) and len(predicted_rainfall) > 0:
                    predicted_rainfall_value = predicted_rainfall[0]
                    st.success(f"Predicted rainfall for {selected_date_str}: {predicted_rainfall_value:.2f} inches")
                else:
                    st.error(f"Unexpected structure in predicted rainfall data: {predicted_rainfall}")
            
            except KeyError as e:
                st.error(f"")
            except Exception as e:
                st.error(f"")
            # except KeyError as e:
            #     st.error(f"KeyError: Missing key {e}")
            # except Exception as e:
            #     st.error(f"An error occurred: {e}")
        
        else:
            st.warning("Selected date is outside the forecast range. Please choose a date within the next five days.")

        # Generate and display data basis rainfall data for the next 7 days
        st.subheader("Data basis Rainfall Predictions for the Next 7 Days")
        rainfall_predictions = generate_rainfall_predictions(selected_date, num_days=7)

        # Display the databasis rainfall predictions for the next 7 days
        st.write(f"Rainfall Forecast from {selected_date} to {selected_date + timedelta(days=6)}:")
        for forecast_date, rainfall in rainfall_predictions.items():
            st.write(f"Date: {forecast_date} - Predicted Rainfall: {rainfall} inches")

    elif page == "Manual Usage":
        st.title("Manual Usage")
        # Add content for the Manual Usage page
        manual.manual()

    elif page == "About Us":
        st.title("About Us")
        about_me.aboutMe()
        header_footer.create_footer()

if __name__ == "__main__":
    main()
