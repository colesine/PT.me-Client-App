import streamlit as st
from PIL import Image
import requests
from streamlit_extras.switch_page_button import switch_page

# Main content
st.title("WORKOUTS")


def resize_and_crop(url, target_width=400, target_height=200):
    # Open the image file
    with Image.open(requests.get(url, stream=True).raw) as img:
        # Calculate the target aspect ratio (2:1)
        target_aspect_ratio = target_width / target_height

        # Get the original image's width and height
        original_width, original_height = img.size
        original_aspect_ratio = original_width / original_height

        # Determine how to resize the image to maintain the aspect ratio
        if original_aspect_ratio > target_aspect_ratio:
            # Image is wider than the target aspect ratio
            new_height = target_height
            new_width = int(new_height * original_aspect_ratio)
        else:
            # Image is taller than the target aspect ratio
            new_width = target_width
            new_height = int(new_width / original_aspect_ratio)

        # Resize the image
        img = img.resize((new_width, new_height), Image.BILINEAR)

        # Calculate coordinates to crop the image to the target size
        left = (new_width - target_width) / 2
        top = (new_height - target_height) / 2
        right = (new_width + target_width) / 2
        bottom = (new_height + target_height) / 2

        # Crop the image
        img = img.crop((left, top, right, bottom))

        return img


def workout_container(image_url, header, subheader, duration):
    with st.container(height=200):
        col1, col2 = st.columns(2)
        with col1:
            st.image(resize_and_crop(image_url), use_column_width=True)
        with col2:
            st.header(header)
            st.subheader(subheader)
            st.write(f"⏱️ {duration} mins")

# Placeholder for main content

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
nav_bar = st.tabs(["To Complete", "Completed"])

# Customize each tab section based on what page you want to display
with nav_bar[0]:
    for workout, data in workouts.items():
            workout_container(data["image"], workout, data["muscles"], data["duration"])

with nav_bar[1]:
    for workout, data in workouts.items():
        workout_container(data["image"], workout, data["muscles"], data["duration"])