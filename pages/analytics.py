import streamlit as st
from datetime import datetime, timedelta
from navbar import navbar
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.stylable_container import stylable_container

# Set page config
st.set_page_config(
    page_title="Analytics",
    initial_sidebar_state="collapsed"
)

def show_info_popup():
    st.info("**Color Scheme Explanation:**\n\n"
            "🟢 **Green (Micro)**: Represent short-term fluctuations, influenced daily by immediate factors.\n\n"
            "🟡 **Yellow (Macro)**: Represents medium-term trends, best observed over weeks to months. Typically reflective of sustained lifestyle habits.\n\n"
            "🔴 **Red (Mega)**: Represents long-term changes or consistent patterns, capturing the overarching direction of a person's health and fitness journey.")

col1, col2 = st.columns([0.8, 0.2])  # Adjust column width ratio as needed

with col1:
    st.subheader("Analytics")

with col2:
    show_info = st.button("ℹ️")
    
if show_info:
    show_info_popup()

# Define CSS styles for each category
css_green = """
button {
    background-color: #27ae60;
    color: white;
    font-weight: bold;
    width: 100%;
    height: 60px;
    border-radius: 8px;
}
"""

css_yellow = """
button {
    background-color: #f1c40f;
    color: white;
    font-weight: bold;
    width: 100%;
    height: 60px;
    border-radius: 8px;
}
"""

css_red = """
button {
    background-color: #e74c3c;
    color: white;
    font-weight: bold;
    width: 100%;
    height: 60px;
    border-radius: 8px;
}
"""

# Metrics data with last updated timestamps
metrics = [
    {"name": "Weight", "value": "78 kg", "color": "yellow", "last_updated": datetime.now()},
    {"name": "Volume", "value": "12,000 kg", "color": "green", "last_updated": datetime.now() - timedelta(hours=2)},
    {"name": "Steps", "value": "8,456", "color": "green", "last_updated": datetime.now() - timedelta(hours=4)},
    {"name": "1 Rep Max", "value": "100 kg", "color": "yellow", "last_updated": datetime.now() - timedelta(hours=6)},
    {"name": "Progress Photos", "value": "12 photos", "color": "red", "last_updated": datetime.now() - timedelta(hours=8)},
    {"name": "Body Composition", "value": "18% BF", "color": "red", "last_updated": datetime.now() - timedelta(hours=10)}
]

# Sort metrics by last updated time
metrics.sort(key=lambda x: x["last_updated"], reverse=True)

# Display each metric with predefined styles based on color
for metric in metrics:
    # Choose the CSS style based on color category
    if metric["color"] == "green":
        css_style = css_green
    elif metric["color"] == "yellow":
        css_style = css_yellow
    elif metric["color"] == "red":
        css_style = css_red
    
    # Apply CSS style to the container
    with stylable_container(metric["color"], css_styles=css_style):
        button_clicked = st.button(f"{metric['name']}: {metric['value']} →", key=metric['name'])
        
        # Redirect if specific button is clicked
        if button_clicked:
            if metric["name"] == "Weight":
                switch_page("weight")  # Redirect to "weight" page
            else:
                pass

navbar()