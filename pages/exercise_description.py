import streamlit as st

# Set page config
st.set_page_config(page_title="Exercise", layout="centered",
    initial_sidebar_state="collapsed")

st.write("# 1 Bench Press (Barbell)")
st.video("assets/2024-11-06 21.49.20.mp4",loop=True, autoplay=True,muted=True)
st.write("**Targets**: Chest, Triceps")

st.write("### Instructions")
instructions = [
    "Lie flat on the bench with feet firmly on the ground.",
    "Grip the barbell slightly wider than shoulder-width apart.",
    "Slowly lower the barbell to your chest, keeping elbows at a 45-degree angle.",
    "Press the barbell back up to the starting position, fully extending your arms."
]

# Display instructions as a numbered list
for i, instruction in enumerate(instructions, start=1):
    st.write(f"{i}. {instruction}")