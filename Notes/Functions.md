---
tags:
  - programming-level-1-2
  - notes
---

# Functions

A function is a block of code that can be reused over and over again.

We can input data to the function. We refer to the data as **parameters**.

We describe the parameters in the docstring. A docstring (is short for
documentation string) tells a human what the purpose of the function is.

We use the term **arguments** to describe the ACTUAL data that we put
into the function.

```python
def area_of_a_square(sidelength: float):
	"""Calculate and print the area of a square.
	Results are in units squared.

	Params:

	sidelength - length of one side of the square
	"""

	area = sidelength ** 2

	print(f"The area of a square with side length {sidelength} is: {area} square units.")

area_of_a_square(12.2)
```