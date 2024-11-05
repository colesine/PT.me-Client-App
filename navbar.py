import streamlit as st
from streamlit_extras.switch_page_button import switch_page

def navbar():
    # Define page names and query parameters
    pages = {
        "Log": "log",
        "Analytics": "analytics",
        "Dashboard": "app",
        "Workouts": "workouts",
        "Profile": "profile",
    }

    # Create a container for the navbar
    with st.container():  
        # Use columns to align buttons in a single row
        cols = st.columns(len(pages))
        
        # Create each button with a link to set the page query parameter
        for col, (label, page_name) in zip(cols, pages.items()):
            with col:
                if st.button(label, use_container_width=True):
                    switch_page(page_name)