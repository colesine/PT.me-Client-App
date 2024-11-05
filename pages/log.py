import streamlit as st
import datetime

# Set page config
st.set_page_config(page_title="Fitness Metrics Dashboard")

# Add custom CSS
st.markdown("""
<style>
    .metric-title {
        font-size: 0.875rem;
        color: #666;
        font-weight: bold;
        text-transform: uppercase;
        margin-bottom: 0.5rem;
    }
    .metric-value {
        font-size: 1.5rem;
        font-weight: bold;
        margin: 0;
        line-height: 1.2;
    }
    .metric-subtitle {
        font-size: 0.75rem;
        color: #666;
        margin-top: 0.5rem;
    }
    .stButton>button {
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'weight' not in st.session_state:
    st.session_state.weight = 75.4
if 'height' not in st.session_state:
    st.session_state.height = 183
if 'steps' not in st.session_state:
    st.session_state.steps = 8775
if 'calories' not in st.session_state:
    st.session_state.calories = 374
if 'heart_rate' not in st.session_state:
    st.session_state.heart_rate = 155
if 'floors' not in st.session_state:
    st.session_state.floors = 3
if 'stress' not in st.session_state:
    st.session_state.stress = 32
if 'intensity' not in st.session_state:
    st.session_state.intensity = 115
if 'note' not in st.session_state:
    st.session_state.note = "Your body will achieve what your mind will believe."

# Title
st.title("Fitness Metrics Dashboard")

  
# Function to switch pages
def switch_page(page_name):
    st.session_state['page'] = page_name

# Edit Metrics Button
if st.button("Edit Metrics"):
    st.switch_page("pages/edit-log.py")


# Create 3x3 grid
col1, col2, col3 = st.columns(3)

# Weight Card
with col1:
    st.markdown('<div class="w3-container">', unsafe_allow_html=True)
    st.markdown('<div><p class="metric-title">WEIGHT</p><p class="metric-value">{:.1f} KG</p></div>'.format(st.session_state.weight), unsafe_allow_html=True)
    st.markdown('<p class="metric-subtitle">Weight</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Height Card
with col2:
    st.markdown('<div class="w3-container">', unsafe_allow_html=True)
    st.markdown('<div><p class="metric-title">HEIGHT</p><p class="metric-value">{} cm</p></div>'.format(st.session_state.height), unsafe_allow_html=True)
    st.markdown('<p class="metric-subtitle">Height</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Notes Card
with col3:
    st.markdown('<div class="w3-container">', unsafe_allow_html=True)
    st.markdown('<div><p class="metric-title">NOTES</p><p class="metric-value" style="font-size: 1rem; line-height: 1.2;">{}</p></div>'.format(st.session_state.note), unsafe_allow_html=True)
    st.markdown('<p class="metric-subtitle">Posted on {}</p>'.format(datetime.datetime.now().strftime("%Y/%m/%d %H:%M")), unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Steps Card
with col1:
    st.markdown('<div class="w3-container">', unsafe_allow_html=True)
    st.markdown('<div><p class="metric-title">STEPS</p><p class="metric-value">{}</p></div>'.format(f"{st.session_state.steps:,}/10,000"), unsafe_allow_html=True)
    st.markdown('<p class="metric-subtitle">Steps</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Calories Card
with col2:
    st.markdown('<div class="w3-container">', unsafe_allow_html=True)
    st.markdown('<div><p class="metric-title">CALORIES</p><p class="metric-value">{}</p></div>'.format(st.session_state.calories), unsafe_allow_html=True)
    st.markdown('<p class="metric-subtitle">Calories Burned</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Heart Rate Card
with col3:
    st.markdown('<div class="w3-container">', unsafe_allow_html=True)
    st.markdown('<div><p class="metric-title">HEART RATE</p><p class="metric-value">{} bpm</p></div>'.format(st.session_state.heart_rate), unsafe_allow_html=True)
    st.markdown('<p class="metric-subtitle">Average</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Floors Card
with col1:
    st.markdown('<div class="w3-container">', unsafe_allow_html=True)
    st.markdown('<div><p class="metric-title">FLOORS</p><p class="metric-value">{}</p></div>'.format(f"{st.session_state.floors}/10"), unsafe_allow_html=True)
    st.markdown('<p class="metric-subtitle">Floors Climbed</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Stress Card
with col2:
    st.markdown('<div class="w3-container">', unsafe_allow_html=True)
    st.markdown('<div><p class="metric-title">STRESS</p><p class="metric-value">{}</p></div>'.format(f"{st.session_state.stress}/100"), unsafe_allow_html=True)
    st.markdown('<p class="metric-subtitle">Stress Levels</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Intensity Card
with col3:
    st.markdown('<div class="w3-container">', unsafe_allow_html=True)
    st.markdown('<div><p class="metric-title">INTENSITY</p><p class="metric-value">{}</p></div>'.format(f"{st.session_state.intensity}/150"), unsafe_allow_html=True)
    st.markdown('<p class="metric-subtitle">Intensity Minutes</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
from navbar import navbar
navbar()
