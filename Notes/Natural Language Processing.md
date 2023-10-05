---
tags:
  - notes
  - natural-language-processing
  - y2023
  - programming-level-1-2
---
# Natural Language Processing
## Output
We can use a function to display text and symbols to the screen
We use the `print()` function to display output

```python
print("Your text goes in here.")
```

> Task
> 1. open Visual Studio Code
> 2. make sure that it's open to your repository
> 3. create a new file called `input_and_output.py`

## [[Headers]]

## Comments
Comments are pieces of text that are *not* interpreted by Python.
This means that the text is **ignored**.  
We use the # symbol to make comments.

```python
# This is a comment
```

> Task
> 1.  In `input_and_output.py1`
> 	1. Put the header
> 	2. Write in some comments

## Input
We grab information from the user using `input()`.  
When we run the function, it does two things:
1. It **waits** for the user to write something or nothing
2. The user presses **Enter/Return** to indicate that they're finished

```python
input()

input(<prompt>)      # prints out the prompt then waits
```

## Variables
Variables allow us to **store** information for the time that our app
is running.

```python
favourite_food = input("What is your favourite food? ")
```

`favourite_food` -> name of the variable
`=` -> assignment operator
`input...` -> value
### Naming
What you can do:
1. name them with letters, numbers, underscores
2. names **should** start with a lowercase letter
What you can't do:
1. you **can't** name them with spaces or symbols
2. you **can't** name them with certain names that are reserved
	1. e.g. `if`, `while`, `for`, `and`, `or`, ...

A good name is something like this:
```python
favourite_food 
fave_food
date_of_birth
student_number
screen_size
```

Bad names are like this:
```python
Favourite_food
a
num
aa
aaa
aaaa
```
# [[Strings]]

# [[Design]]

# [[List|Lists]]

# [[Modules]]
