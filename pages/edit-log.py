import streamlit as st

# Set page config
st.set_page_config(page_title="Edit Fitness Metrics", layout="wide")

# Title
st.title("Edit Fitness Metrics")

# Save and Return Button
if st.button("Save and Return to Logs"):
    st.switch_page("pages/log.py")

# Create 3x3 grid
col1, col2, col3 = st.columns(3)

# Weight Input
with col1:
    st.number_input("Weight (KG)", value=st.session_state.weight, step=0.1, key="weight_input", on_change=lambda: setattr(st.session_state, 'weight', st.session_state.weight_input))

# Height Input
with col2:
    st.number_input("Height (cm)", value=st.session_state.height, step=1, key="height_input", on_change=lambda: setattr(st.session_state, 'height', st.session_state.height_input))

# Notes Input
with col3:
    st.text_area("Add a note", value=st.session_state.note, key="note_input", on_change=lambda: setattr(st.session_state, 'note', st.session_state.note_input))

# Steps Input
with col1:
    st.number_input("Steps", value=st.session_state.steps, step=1, key="steps_input", on_change=lambda: setattr(st.session_state, 'steps', st.session_state.steps_input))

# Calories Input
with col2:
    st.number_input("Calories Burned", value=st.session_state.calories, step=1, key="calories_input", on_change=lambda: setattr(st.session_state, 'calories', st.session_state.calories_input))

# Heart Rate Input
with col3:
    st.number_input("Heart Rate (bpm)", value=st.session_state.heart_rate, step=1, key="heart_rate_input", on_change=lambda: setattr(st.session_state, 'heart_rate', st.session_state.heart_rate_input))

# Floors Input
with col1:
    st.number_input("Floors Climbed", value=st.session_state.floors, step=1, key="floors_input", on_change=lambda: setattr(st.session_state, 'floors', st.session_state.floors_input))

# Stress Input
with col2:
    st.number_input("Stress Level", value=st.session_state.stress, step=1, min_value=0, max_value=100, key="stress_input", on_change=lambda: setattr(st.session_state, 'stress', st.session_state.stress_input))

# Intensity Input
with col3:
    st.number_input("Intensity Minutes", value=st.session_state.intensity, step=1, key="intensity_input", on_change=lambda: setattr(st.session_state, 'intensity', st.session_state.intensity_input))

