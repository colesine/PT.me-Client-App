import streamlit as st
from datetime import datetime
from resize_crop import resize_and_crop
from navbar import navbar

# Set page config
st.set_page_config(
    page_title="PT.me Profile",
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

# Profile Section
st.write("# Your Profile")
with st.container(height=240):
    col1, col2 = st.columns([1, 2],vertical_alignment="center")
    with col1:
        st.image(resize_and_crop("https://img.freepik.com/premium-photo/portrait-photo-chinese-teenage-male-straight-hair_662214-131847.jpg",200,200))
    with col2:
        st.write("## Julius Ang")
        st.write("### Start Date: 11/11/2024")
        st.write("### Training Mode: Hybrid")

# Achievements section - single row with horizontal scroll
st.subheader("My Achievements")
with st.container():
    col1, col2, col3, col4 = st.columns(4)
    for i, col in enumerate([col1, col2, col3, col4], start=1):
        with col:
            st.button(f"# 🏆",key=i)


# Coach section
st.subheader("My Coach: Jane Wong")
coach_col1, coach_col2 = st.columns([1, 2])
with coach_col1:
    st.image("assets/coach.jpeg", width=220)  # Local image for coach
with coach_col2:
    st.write("""
        ### Jane Wong
        
        **Specialized in:**
        - Weight loss, general health, muscle building
        
        **Certifications:**
        - ACE Certified Personal Trainer
        - Nutrition Specialist
        - Strength & Conditioning Expert
        
        Jane is a dedicated coach who has helped over 100 clients to date. Having lost weight herself, she understands the challenges and helps clients achieve their goals through personalized programs.
        """)

# Stats section
st.subheader("My Stats")
stats_col1, stats_col2, stats_col3 = st.columns(3)

with stats_col1:
    st.metric("Height", "175 cm")
with stats_col2:
    st.metric("Weight", "70 kg")
with stats_col3:
    st.metric("Body Fat", "15%")

# Linked devices section
st.subheader("Linked Devices and Accounts")
linked_devices_container = st.container()
with linked_devices_container:
    ld_col1, ld_col2, ld_col3, ld_col4 = st.columns(4)
    with ld_col1:
        st.image("assets/apple_health.png", width=60)  # Local image for Apple Health
    with ld_col2:
        st.image("assets/fitbit.png", width=60)  # Local image for Fitbit
    with ld_col3:
        st.image("assets/google_health.png", width=60)  # Local image for Google Health
    with ld_col4:
        st.image("assets/myfitnesspal.png", width=60)  # Local image for MyFitnessPal


navbar()