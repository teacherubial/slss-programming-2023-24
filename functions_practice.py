# Functions Practice
# Author: Ubial
# 24 November 2023


def area_of_a_square(sidelength: float) -> float:
    """Return the area of a square.
    Results are in units squared.

    Params:

    sidelength - length of one side of the square
    """

    area = sidelength**2

    return area


def print_area_of_a_square(sidelength: float) -> None:
    """Calculate and print the area of a square.
    Results are in units squared.

    Params:

    sidelength - length of one side of the square
    """

    area = sidelength**2

    print(
        f"The area of a square with side length {sidelength} is: {area} square units."
    )


# print_area_of_a_square(12.2)
# print_area_of_a_square(12)

# Given two squares of two sidelengths
#    12.2 and 144
# Add the area of both squares

print(area_of_a_square(10.5))


# Question 1:
# Create a function called stars()
# Takes an int as a parameter
# Returns a string of stars of given length
# Aside: Signature of a function
#     - name of the function
#     - inputs/parameters / type
#     - return type
def stars(num_stars: int) -> str:
    """Returns a number of stars

    Params:

    num_stars - the number of stars to return
    """

    return "*" * num_stars


print(stars(5))

# Question 2:
# Create a function called biggest_of_three()
# Takes three parameters, all floats
# Returns the biggest one


def biggest_of_three(num_one: float, num_two: float, num_three: float) -> float:
    """Returns the biggest of three given numbers.

    Params:
    num_one - the first number
    num_two - the second number
    num_three - the third number

    Returns:
    the biggest of the three numbers
    """
    if num_one > num_two and num_one > num_three:
        return num_one
    elif num_two > num_three:
        return num_two
    else:
        return num_three


print(biggest_of_three(1000, 100, 10))
print(biggest_of_three(100, 1000, 10))
print(biggest_of_three(10, 100, 1000))

# Question 3
# Question 4
# Create functions called pyramid() and pyramid_mirror()
# Takes one number as a parameter
# Give a pyramid either regular way or mirrored


def pyramid(num_layers: int) -> None:
    """Prints out a pyramid of given number of layers.

    Params:
    num_layers - number of layers in the pyramid
    """

    for current_layer in range(1, num_layers + 1):
        print(stars(current_layer))


pyramid(2)
pyramid(3)
pyramid(20)


def pyramid_mirror(num_layers: int) -> None:
    """Prints out a mirrored pyramid.

    Params:
    num_layers - number of layers of pyramid
    """

    for current_layer in range(1, num_layers + 1):
        # Print the spaces then print the stars
        # num_layers == 2
        # " " * 1  +  stars(1)
        # " " * 0   + stars(2)
        # num_layers == 3
        # " " * 2  + stars(1)
        # " " * 1  + stars(2)
        # " " * 0  + stars(3)
        print(" " * (num_layers - current_layer) + stars(current_layer))


pyramid_mirror(4)
pyramid_mirror(20)
