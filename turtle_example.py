# Turtle Example
# Author: Ubial
# 21 November 2023

import turtle

# Create a turtle that can be moved around the screen

FORWARD_MAGNITUDE = 20

# Make a turtle object
michaelangelo = turtle.Turtle()

# Get some input from the user
print("""To give commands, type:
F - to go forward
L - to turn left
R - to turn right.""")

# Repeat the below forever, or until the user says stop
done = False

while not done:
    command = input("Where should I go? ").strip(",.?! ").lower()

    # Move the turtle around based on that input
    # Stop if the user says stop
    if command in ["f", "forward"]:
        michaelangelo.forward(FORWARD_MAGNITUDE)
    elif command in ["l", "left"]:
        michaelangelo.left(90)  
    elif command in ["r", "right"]:
        michaelangelo.right(90)
    elif command == "stop":
        done = True
    