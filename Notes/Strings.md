Strings are a [[Type]] of data

# Format Strings
If we want to evaluate inside of a string, we use *f-strings*.  
To create an f-string, we put an `f` before the open quote

```python
fave_food = input("What's your favourite food? ")

print(f"Ooooooo, {fave_food} sounds good!")
```

# String Methods

[[Methods]] are functions that we can use on [[objects]].

String methods allow us to modify strings.

Say for example, we want to make all the characters of
a string lowercase.

```python
mr_ubial_yelling = "YOU SHOULD PUSH YOUR CHAIRS IN"

print(mr_ubial_yelling.lower())
```

The `.lower()` method takes a string and converts all uppercase
characters to lowercase.