Imagine that you want your code to do something only if a certain condition is met

We can do this using conditionals  
When we use a conditional, we create branches of code  

![Sacred Timeline](https://www.xfire.com/wp-content/uploads/2021/07/Marvel-Loki-Alternate-Multiverse-Sacred-Timeline-Kang.jpg)

In Python we do the following to create a branch of code:

```python
if <boolean expression>:
	<block of code>
elif <boolean expression>:
	<block of code>
else:
	<block of code>
```

**[[Boolean]] expressions** are pieces of Python code that either are a boolean value (`True`, `False`) or they *evaluate* to become a boolean.

The whole block of code will run if and only if the boolean expression produces `True`.

`if` and `elif` require a boolean expression to run, whereas `else` will catch every other case.

The following is a trivial example that shows how *boolean* values influence which blocks of code will run. Predict what you think will happen.

```python
if True:
	print("This will print out.")
else:
	print("No! This will print out.")
```

An example snippet using *conditionals* looks like this.

```python
import random

# Ask the user what their favourite food is
fave_food = input("What's your favourite food? ")

# If they answer pizza, say that's my favourite too!
if fave_food == "pizza":
	print("Pizza is my favourite! The best place to go for pizza is Best Pizza in Brooklyn.")
elif fave_food == "pasta":
	print("Mmmm. Pasta is good too.")
else:
	list_of_food_responses = [
		"I've never tried that before.",
		"That sounds good.",
		"Yum!"
	]
	print(random.choice(list_of_food_responses))

```