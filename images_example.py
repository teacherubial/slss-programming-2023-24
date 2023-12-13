# Images and Python
# Author: Ubial
# 11 December 2023

from PIL import Image

# Recall that we can open up files in Python
with Image.open("./Images/kid-green.jpg") as im:
    # get the pixel information from the top left most pixel
    pixel = im.getpixel((0, 0))

    # print the pixel information
    print(pixel)

    # get the middle pixel
    middle = im.width
