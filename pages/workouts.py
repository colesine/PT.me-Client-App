import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from navbar import navbar
from resize_crop import resize_and_crop

# Main content
st.set_page_config(page_title="Workouts", page_icon="📈")

def workout_container(image_url, header, subheader, duration, key):
    with st.container(height=280):
        col1, col2 = st.columns(2)
        with col1:
            st.image(resize_and_crop(image_url), use_column_width=True)
        with col2:
            st.header(header)
            st.subheader(subheader)
            st.write(f"⏱️ {duration} mins")
            do_workout = st.button("Get Started", key=f"{key}_button")
            if do_workout:
                switch_page("workout")

# Define workouts
workouts = {
    "Push Day": {
        "image": "https://hips.hearstapps.com/hmg-prod/images/man-training-with-dumbbells-royalty-free-image-1690233265.jpg?crop=0.668xw:1.00xh;0.145xw,0&resize=640:*",
        "muscles": "Chest, Triceps",
        "duration": "55"
    },
    "Push Day 2": {
        "image": "https://hips.hearstapps.com/hmg-prod/images/man-training-with-dumbbells-royalty-free-image-1690233265.jpg?crop=0.668xw:1.00xh;0.145xw,0&resize=640:*",
        "muscles": "Chest, Triceps",
        "duration": "55"
    }
}

# Setting up a navbar using tabs in Streamlit
is_completed = st.tabs(["To Complete", "Completed"])

# Customize each tab section based on what page you want to display
with is_completed[0]:
    for index, (workout, data) in enumerate(workouts.items()):
        workout_container(data["image"], workout, data["muscles"], data["duration"], key=f"to_complete_{index}")

with is_completed[1]:
    pass

navbar()