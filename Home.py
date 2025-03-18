import streamlit as st

# Add a theme toggle switch
dark_mode = st.sidebar.toggle("🌙 Dark Mode")

# Apply dark mode if enabled
if dark_mode:
    st.markdown(
        """
        <style>
            body {
                background-color: #121212;
                color: white;
            }
            .stTextInput, .stButton {
                color: white !important;
                background-color: #333333 !important;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
