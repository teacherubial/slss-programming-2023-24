In Python, data can be grouped in categories called Types.

| Name             | Example         |
| ---              | ---             |
| string           | `"hello"`          |
| list             | `[1, 2, 3, 4]`     |
| integers or `int`  | `1`  `-10`  `23`    | 
| `float`            | `3.5`  `-3.5`  `1.0` |
| boolean or `bool`  | `True` `False`      |

An example of using these types of data:

```python
favourite_food = "tempura"
my_age = 16      # my_age is of type int or integer
```

## Converting Types

There are some **special functions** built in to Python that helps to convert data from one type to another.

```python
intro_string = "My age is"
my_age = 16

# Recall
"My name is" + "Jim"        # "My name isJim"
"My name is" + " " + "Jim"  # "My name is Jim"
intro_string + my_age       # This is going to BREAK
```