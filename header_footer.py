import streamlit as st

# Function to create a beautiful header
def create_header():
    st.title("Rainfall forecasting using rnn")
    st.image("rainfall.png", use_container_width=True)


# Function to create a beautiful footer
def create_footer():
    st.write(
        """
        ---
        ### Contact Information
        For inquiries, please contact us at [snuhithanguluri27@gmail.com, princetimothy137@gmail.com].
        
        """
    )