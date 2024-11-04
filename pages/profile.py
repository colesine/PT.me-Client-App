import streamlit as st
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="PT.me Profile",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
    <style>
/* Force single row for achievements */
    .achievement-container {
        display: flex;
        flex-direction: row;
        justify-content: flex-start;
        gap: 20px;
        overflow-x: auto;
        padding: 10px 0;
        margin: 20px 0;
        -webkit-overflow-scrolling: touch;
    }
    
    .achievement-item {
        flex: 0 0 auto;
        width: 60px;
        height: 60px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
    }
    
    /* Center profile container */
    .profile-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 20px;
        max-width: 600px;
        margin: 0 auto;
        text-align: center;
    }

    /* Profile image styling */
    .profile-image {
        width: 100px;
        height: 100px;
        border-radius: 50%;
        background-color: #f0f0f0;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 40px;
        margin-bottom: 20px;
    }

    /* Info box styling */
    .info-box {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)


st.markdown("""
    <div class='profile-container'>
        <h1>Your Profile</h1>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <div class='profile-image profile-container'>👤</div>
    <div class='profile-container'>
        <h2>Julius Ang</h2>
    </div>
    """, unsafe_allow_html=True)
            
# Profile info box
st.markdown("""
    <div class='info-box'>
        <p><strong>Start Date:</strong> 01/01/2024</p>
        <p><strong>Training Mode:</strong> On-site</p>
    </div>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)


# Achievements section - single row with horizontal scroll if needed
st.subheader("My Achievements")
st.markdown("""
    <div class='achievement-container'>
        <div class='achievement-item'>🏆</div>
        <div class='achievement-item'>🏅</div>
        <div class='achievement-item'>💪</div>
        <div class='achievement-item'>🚩</div>
    </div></br>
""", unsafe_allow_html=True)

# Coach section
st.subheader("My Coach: Jane Wong")
coach_col1, coach_col2 = st.columns([2, 3])


with coach_col1:
    st.markdown("<img src='./assets/coach.jpeg' style='width: 150px; height: 150px;'>", unsafe_allow_html=True)
with coach_col2:
    if st.button("Jane Wong"):
        st.markdown("""
        ### Jane Wong
        
        **Specialized in:**
        - Weight loss, general health, muscle building
        
        **Certifications:**
        - ACE Certified Personal Trainer
        - Nutrition Specialist
        - Strength & Conditioning Expert
        
        Jane is a dedicated coach who has helped over 100 clients to date. Having lost weight himself, he understands the challenges and helps clients achieve their goals through personalized programs.
        """)

st.markdown("</br></br>", unsafe_allow_html=True)

# Stats section
st.subheader("My Stats")
stats_col1, stats_col2, stats_col3 = st.columns(3)

with stats_col1:
    st.metric("Height", "175 cm")
with stats_col2:
    st.metric("Weight", "70 kg")
with stats_col3:
    st.metric("Body Fat", "15%")

#need to sync up with session state data?

st.markdown("</br></br>", unsafe_allow_html=True)

# Linked devices section
st.subheader("Linked Devices and Accounts")
st.markdown("""
    <div class='achievement-container'>
        <div class='achievement-item'><img src='assets/apple_health.png'></div>
        <div class='achievement-item'><img src='assets/fitbit.png'></div>
        <div class='achievement-item'><img src='assets/google_health.png'></div>
        <div class='achievement-item'><img src='assets/myfitnesspal.png'></div>
    </div>
""", unsafe_allow_html=True)