import streamlit as st
from datetime import datetime, timedelta

# Set page config
st.set_page_config(
    page_title="Analytics",
    layout="wide",
    initial_sidebar_state="collapsed"
)
# Custom CSS for styling
st.markdown("""
    <style>
    /* Card container */
    .metric-card {
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        cursor: pointer;
        transition: transform 0.2s;
    }
    .metric-card:hover {
        transform: translateX(5px);
    }
    
    /* Background colors */
    .bg-yellow {
        background-color: #FFC300;
    }
    .bg-green {
        background-color: #006400;
    }
    .bg-red {
        background-color: #8B0000;
    }
    
    /* Header styling */
    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem;
        border-bottom: 1px solid #eee;
        margin-bottom: 2rem;
    }
    
    /* Navigation bar */
    .nav-bar {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        display: flex;
        justify-content: space-around;
        padding: 1rem;
        background: white;
        border-top: 1px solid #eee;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="header">
        <h1>PT.me</h1>
        <div>🔔</div>
    </div>
""", unsafe_allow_html=True)

# Analytics section
st.subheader("Analytics")

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

# Display metrics as cards
for metric in metrics:
    card_html = f"""
        <div class="metric-card bg-{metric['color']}">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <div style="font-size: 1.1rem; font-weight: 500;">{metric['name']}</div>
                    <div style="color: #ffffff;">{metric['value']}</div>
                </div>
                <div>→</div>
            </div>
        </div>
    """
    if metric["name"] == "Weight":
        # Wrap the card in a link to the weight page
        card_html = f'<a href="weight" style="text-decoration: none;">{card_html}</a>'
    st.markdown(card_html, unsafe_allow_html=True)
