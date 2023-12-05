# Functions and Turtle
# Author: Brant
# 28 November 2023

import turtle

burt = turtle.Turtle()
turtle.tracer(0, 0)  # Turn off animation, set delay to 0

burt.color("lightblue")


def squared(num: float) -> float:
    """Takes a number and squares and returns it."""

    return num**2


def draw_square(side_length: int) -> None:
    """Draw a square of a given length."""
    burt.forward(side_length)
    burt.left(90)
    burt.forward(side_length)
    burt.left(90)
    burt.forward(side_length)
    burt.left(90)
    burt.forward(side_length)
    burt.left(90)


def draw_tree(level: int, height: int) -> None:
    """A recursive function that draws a tree
    with initial given height in pixels

    Params:

    level - number representing the levels of branches
    height - height of the main trunk in pixels
    """

    if level > 0:
        burt.forward(height)
        burt.left(36)
        draw_tree(level - 1, height * 0.75)
        burt.right(36 * 2)
        draw_tree(level - 1, height * 0.75)
        burt.left(36)
        burt.back(height)
    else:
        original_colour = burt.color()
        burt.color("green")
        burt.stamp()
        burt.color(original_colour[0])


burt.color("brown")
burt.setheading(90)
burt.pu()
burt.back(200)
burt.pd()
burt.width(4)
burt.speed("fastest")

draw_tree(10, 175)

turtle.update()  # Update the drawing only after tree is completely drawn
turtle.done()
