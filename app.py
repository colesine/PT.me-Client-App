import streamlit as st
from navbar import navbar
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

# Configure the page
st.set_page_config(page_title="PT.me Dashboard", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    .achievement-banner {
        background-color: #573a6b;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .workout-banner {
        background-color: #000000;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
        margin-bottom: 20px;
        cursor: pointer;
    }
    .progress-banner {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
    }
    
        .rat-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 20px;
        background-color: #f0f2f6;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .rat-caption {
        font-size: 18px;
        font-weight: bold;
        margin-top: 10px;
        text-align: center;
    }
    .care-button {
        margin-top: 20px;
    }
    
    .center {
        display: flex;
        justify-content: center;
        text-align: center;
        center-align: center;
    }
    
    </style>
    """, unsafe_allow_html=True)

# Achievement Banner
st.markdown("""
    <div class="achievement-banner">
        <h2>🎉 CONGRATULATIONS!</h2>
        <p style='font-size: 18px;'>You have lost <span style='color: #ff4b4b;'>10%</span> of your body weight with Coach Jane Wong since you started!</p>
        <button style='background-color: #331d47; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;'>
            Share your achievement
        </button>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

#Rat

st.markdown("""<div class='center'>""",unsafe_allow_html=True)

# Display rat image
# Assuming the image is in a folder named 'images' in the same directory as this script
rat_image_url = "assets/rat_logo.jpg"  # Replace with actual rat image URL
st.image(rat_image_url, caption="", width=100)


# Caption
st.markdown("<p class='rat-caption'>Your furry friend needs your care and attention!</p>", unsafe_allow_html=True)

# Button to link to rats.py
if st.button("Take Care of Jimmy!", key="care_button", use_container_width=True):
    st.switch_page("pages/rat.py")

st.markdown("</div>", unsafe_allow_html=True)

# Next Workout Banner (with Clickable Button)
st.markdown("""
    <div class="workout-banner" style="position: relative;">
        <h3>Your next workout</h3>
        <div style='display: flex; align-items: center;'>
            <div style='font-size: 24px; margin-right: 10px;'><img src='https://hips.hearstapps.com/hmg-prod/images/man-training-with-dumbbells-royalty-free-image-1690233265.jpg?crop=0.668xw:1.00xh;0.145xw,0&resize=640:*' alt='push-day-workout' width='200px' height='120px'></div>
            <div>
                <h4 style='margin: 0;'>Push day</h4>
                <p style='margin: 0; color: #666;'>Chest, triceps, shoulders</p>
            </div>
        </div>
        <div id="workout-button-container" style="position: absolute; top: 10px; right: 10px;"></div>
    </div>
    """, unsafe_allow_html=True)

# Add a button to the workout banner
workout_button = st.button("View Workout", key="view_workout_button")

# Use JavaScript to move the button into the workout banner
st.markdown("""
    <script>
        const button = document.querySelector('.stButton button');
        const container = document.getElementById('workout-button-container');
        if (button && container) {
            container.appendChild(button);
        }
    </script>
    """, unsafe_allow_html=True)

# If workout button is clicked
if workout_button:
    st.switch_page("pages/workouts.py")
    
    
# Weight Loss Progress
st.markdown("<div>", unsafe_allow_html=True)
st.subheader("Weight Loss Progress")


# Add link to goals page
if st.button("View Goals", key="view_goals_button"):
    st.switch_page("pages/goals.py")

# Create responsive semicircular gauge for current weight
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'indicator'}]])

fig.add_trace(go.Indicator(
    mode="gauge+number",
    value=74.1,
    number={'suffix': "kg", 'font': {'size': 40}},
    gauge={
        'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
        'bar': {'color': "#1f77b4"},
        'bgcolor': "white",
        'borderwidth': 2,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 74.1], 'color': '#1f77b4'}
        ],
        'threshold': {
            'line': {'color': "#57ff5c", 'width': 4},
            'thickness': 0.75,
            'value': 55.6
        },
    },
    domain={'x': [0, 1], 'y': [0, 1]}
))

fig.update_layout(
    autosize=True,
    height=300,
    margin=dict(l=20, r=20, t=50, b=20),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
)

# Use Streamlit's columns to create a responsive layout
col1, col2 = st.columns([2, 1])

with col1:
    # Display the gauge in the larger column
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

with col2:
    # Display progress bars in the smaller column
    st.markdown("### Progress")
    st.markdown("Weekly goal")
    st.progress(0.80, text="80%")
    st.markdown("Ultimate goal")
    st.progress(0.20, text="20%")

st.markdown("</div>", unsafe_allow_html=True)


navbar()