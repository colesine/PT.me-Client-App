import streamlit as st
from PIL import Image
import time
from navbar import navbar

# Initialize session state variables if they don't exist
if 'cheese_count' not in st.session_state:
    st.session_state.cheese_count = 0
if 'current_level' not in st.session_state:
    st.session_state.current_level = 9
if 'rat_state' not in st.session_state:
    st.session_state.rat_state = 1

# Configure the page
st.set_page_config(page_title="PT.me - Jimmy the Gym Rat")

# Custom CSS for styling
st.markdown("""
    <style>
    .stProgress > div > div > div > div {
        background-color: rgb(114, 158, 238);
    }
    .big-font {
        font-size: 24px !important;
        font-weight: bold;
    }
    .game-container {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)


# Main game container
st.markdown("<div>", unsafe_allow_html=True)

# Title and level progress
st.markdown("<h2 style='text-align: center;'>Jimmy the Gym Rat!</h2>", unsafe_allow_html=True)

# Calculate progress percentage
progress = (st.session_state.cheese_count % 3) / 3
current_level = st.session_state.current_level + (st.session_state.cheese_count // 3) * 10

# Display progress bar
st.progress(progress)
st.markdown(f"<p style='text-align: center;'>Level {current_level}</p>", unsafe_allow_html=True)

# Display remaining cheeses needed
cheeses_needed = 3 - (st.session_state.cheese_count % 3)
st.markdown(
    f"<p style='text-align: center;'>{cheeses_needed} more {'cheese' if cheeses_needed == 1 else 'cheeses'} needed to level up</p>",
    unsafe_allow_html=True
)

# Display rat image based on current state
# In a real implementation, you would replace these with actual rat images
rat_images = {
    1: "assets/rat1.jpg",
    2: "assets/rat2.jpg",
    3: "assets/rat3.jpg",
}

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(rat_images[st.session_state.rat_state], caption="", width=200)

# Feed button
def feed_rat():
    st.session_state.cheese_count += 1
    # Change rat state based on cheese count, but stop at state 3
    if st.session_state.rat_state < 3:
        st.session_state.rat_state = min((st.session_state.cheese_count // 3) + 1, 3)
    
    # Add animation effect
    with st.spinner('Feeding Jimmy...'):
        time.sleep(0.5)

# Center the button using columns

if st.button("🧀 Feed Daily Cheese", key="feed_button", use_container_width=True):
    feed_rat()

st.markdown("</div>", unsafe_allow_html=True)

# Display stats
st.markdown("### Stats")
st.write(f"Total Cheese Fed: {st.session_state.cheese_count}")
st.write(f"Current Level: {current_level}")


navbar()