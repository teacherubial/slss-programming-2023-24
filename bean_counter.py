# Jelly Bean Colour Counter
# Author: Ubial
# 9 January 2024

# Version 0.1 ---
# Count all red pixels
# Report on the percentage of all red jellybeans
# Version 0.2 ---
# Count all the green pixels
# Report on the percantge of all green jellybeans
# Version 0.3 ---
# Count all the _____ pixels
# Report on the percentage of all ____ jellybeans

from PIL import Image

import colour_helper

RED_PIXEL = (150, 0, 0)
GREEN_PIXEL = (0, 150, 0)

jelly_bean_img = Image.open("./Images/Jelly Beans.jpg")

red_pixels = []
green_pixels = []

# Visit every pixel in the image
for y in range(jelly_bean_img.height):
    for x in range(jelly_bean_img.width):
        current_pixel = jelly_bean_img.getpixel((x, y))

        if colour_helper.pixel_to_string(current_pixel) == "red":
            red_pixels.append((x, y))
        elif colour_helper.pixel_to_string(current_pixel) == "jelly bean green":
            green_pixels.append((x, y))

# Calculate the percentage of all jelly bean colours
red_percentage = len(red_pixels) / (jelly_bean_img.width * jelly_bean_img.height) * 100
green_percentage = (
    len(green_pixels) / (jelly_bean_img.width * jelly_bean_img.height) * 100
)

# Create a map of all "found" pixels for a respective colour
# Create a new image that is the same size as the original
original_size = (jelly_bean_img.width, jelly_bean_img.height)
green_pixel_map = Image.new("RGB", original_size)

# For every pixel location in "found" pixel list, place a pixel on that new image
for pixel_loc in green_pixels:
    green_pixel_map.putpixel(pixel_loc, GREEN_PIXEL)

green_pixel_map.save("./Images/green_pixel_map.jpg")

green_pixel_map.close()
jelly_bean_img.close()

# Display Report
print(f"Red Jelly Beans: {round(red_percentage, 2)}%")
print(f"Green Jelly Beans: {round(green_percentage, 2)}%")
