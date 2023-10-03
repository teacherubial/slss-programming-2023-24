Booleans are a  [[Type]] of data that is either `True` or `False`

Booleans and [[Conditionals]] work hand-in-hand

They are named after the English mathematician and philosopher, [George Boole](https://en.wikipedia.org/wiki/George_Boole)

Example:
```python
raining = True
sunny = False
```

# Boolean Mathematics

Don't let the name throw you off. Boolean math is, in my opinion, some of the most straightforward math.

Just like with the other maths, it has its symbols (or operators as we call them in programming).

## Binary Operators

Binary operations require **two** boolean values or expressions.

### Equality (`==`)

We use `==` to see if two booleans or boolean operations are **equal to** each other.

```python
True == True         # True!
True == False        # False.
False == True        # False.
False == False       # True!
```

Here's a practical application using equality:

```python
fave_food = input("What's your favourite food? ")

if fave_food == "pizza":
	print("I love pizza!")
```

### `and`

`and` will produce `True` if and only if **both** boolean expressions are `True`.

```python
raining = True
have_umbrella = False

if raining and have_umbrella:  # raining AND have_umbrella need to be true
	print("You came prepared for the weather!")
elif raining:
	print("You should have brought your umbrella. 💧")
```

### `or`

`or` will produce `True` if and only if at least one of the boolean expressions are `True`.

```python
have_bow = True
have_axe = False

if have_bow or have_axe:
	print("I think you're ready to fight the dragon!")
else:
	print("You need to prepare a little more for the quest.")
```

## Unary Operators

Unary operators require only **one** boolean expression.

### `not`

Not allows us to negate a boolean value. In other words, it reverses the boolean.

```python
sunny = False

if not sunny:
	print("You should probably bring your coat.")
```

To elaborate the case above, `not sunny` is the boolean operation. The `not` flips the boolean to the opposite value. Therefore, the code block will execute if and only if `sunny` is `False`.