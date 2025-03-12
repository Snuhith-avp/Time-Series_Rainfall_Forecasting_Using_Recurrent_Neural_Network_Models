import streamlit as st
from datetime import datetime, timedelta
import calculations
import manual, about_me, predict
import header_footer

# Main function
def main():
    # Create a sidebar navigation bar
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select a page", ["Home", "About Us", "Manual Usage"])

    header_footer.create_header()
    # Show different content based on the selected page
    if page == "Home":

        # Rest of your app logic
        st.title("Rainfall forecasting using rnn")
        current_date = datetime.now().date()
        selected_date = st.date_input("Select a date", current_date)
        forecast_start_date = current_date
        forecast_end_date = current_date + timedelta(days=5)
        if forecast_start_date <= selected_date <= forecast_end_date:
            selected_date_str = selected_date.strftime("%Y-%m-%d")
            inputs = calculations.getData(selected_date_str)
            predicted_rainfall = predict.predict_rainfall(inputs)
            predicted_rainfall_value = predicted_rainfall[0]

            # Display the predicted rainfall value
            st.success(f"Predicted rainfall for {selected_date_str}: {predicted_rainfall_value:.2f} inches")
        else:
            st.warning("Selected date is outside the forecast range. Please choose a date within the next seven days.")


    elif page == "About Us":
        st.title("About Us")
        about_me.aboutMe()

    elif page == "Manual Usage":
        st.title("Manual Usage")
        # Add content for the Manual Usage page
        manual.manual()
    header_footer.create_footer()

if __name__ == "__main__":
    main()
