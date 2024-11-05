from PIL import Image
import requests

def resize_and_crop(url, target_width=400, target_height=300):
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