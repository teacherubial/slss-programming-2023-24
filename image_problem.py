# Solutions to Questions about Images
# Author: Ubial
# 20 December 2023

from PIL import Image

import colour_helper


# Question 2: Binarizing an image
def binarize(filename: str) -> None:
    """Binarize a given image that's in the Image folder"""

    with Image.open(f"./Images/{filename}") as im:
        # Visit every pixel
        for y in range(im.height):
            for x in range(im.width):
                pixel = im.getpixel((x, y))

                if colour_helper.is_light(pixel):
                    # replace with white pixel
                    im.putpixel((x, y), colour_helper.WHITE_PIXEL)
                else:
                    # replace with a black pixel
                    im.putpixel((x, y), colour_helper.BLACK_PIXEL)

        # Save the image
        im.save("./Images/binarized.jpg")


def image_to_grayscale(filename: str) -> None:
    """Convert an image to grayscale"""

    with Image.open(f"./Images/{filename}") as im:
        # Visit every pixel
        for y in range(im.height):
            for x in range(im.width):
                pixel = im.getpixel((x, y))

                # Put pixel that is a grayscale version
                im.putpixel((x, y), colour_helper.pixel_to_grayscale(pixel))

        im.save("./Images/grayscale.jpg")


binarize("kid-green.jpg")
image_to_grayscale("best_pizza.jpg")
