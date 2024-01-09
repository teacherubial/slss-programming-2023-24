# Jelly Bean Colour Counter
# Author: Ubial
# 9 January 2024

# Version 0.1
# Count all red pixels
# Report on the percentage of all red

from PIL import Image

import colour_helper

jelly_bean_img = Image.open("./Images/Jelly Beans.jpg")

red_pixels = []

# Visit every pixel in the image
for y in range(jelly_bean_img.height):
    for x in range(jelly_bean_img.width):
        current_pixel = jelly_bean_img.getpixel((x, y))

        # If that pixel is red, store the location
        if colour_helper.pixel_to_string(current_pixel) == "red":
            red_pixels.append((x, y))

# Count every red pixel in the list
# Divide that number by the total pixels in the image
red_percentage = len(red_pixels) / (jelly_bean_img.width * jelly_bean_img.height)
print(red_percentage * 100)
