# Images and Python
# Author: Ubial
# 11 December 2023

import colour_helper

from PIL import Image


# Recall that we can open up files in Python
with Image.open("./Images/kid-green.jpg") as im:
    # algorithm to visit every pixel in the kid-green image
    # store the height and width of the image
    image_height = im.height
    image_width = im.width

    # load the background image
    bg_im = Image.open("./Images/beach.jpg")

    # outer loop is top->bottom
    # inner loop is left->right
    for y in range(image_height):
        for x in range(image_width):
            pixel = im.getpixel((x, y))

            # check pixel if it's green
            if colour_helper.pixel_to_string(pixel) == "green":
                # replace with bg_pixel
                bg_pixel = bg_im.getpixel((x, y))
                im.putpixel((x, y), bg_pixel)

    bg_im.close()

    # save the image
    im.save("./Images/output.jpg")
