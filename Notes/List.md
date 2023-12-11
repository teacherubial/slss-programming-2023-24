A list in Python is a collection of items  
We can store *different* values in a list  
**Order matters** in a list

A list is also a [[Type]] of data
# Creating A List
To make a list, we use brackets \[ \] to surround our list  
We separate out the items using `,`

```python
some_list = ["John", "Tim", "Sara"]
```
# Access Elements in a List
We can grab things from lists using the bracket notation  
In our example above, if I wanted to access `"Tim"`, I would do the following:

```python
some_list[1]      # "Tim"
some_list[2]      # "Sara"
some_list[-1]     # "Sara"
some_list[-2]     # "Tim"
```

Inside the brackets, we say the *index* of the value we want  
Python uses *0-index* counting, which means we start counting at 0

## 2-dimensional List

So far, all the lists we've used in the class are one-dimensional.

```python
some_list = ["red", "blue", "green"]
```

We can create two-dimensional lists, which are lists inside a list.

```python
some_2d_list = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]
#            r  c
some_2d_list[0] [0]     # -> 1
some_2d_list[-1][-1]    # -> 9
```
## Tuples

Tuples (toopels or tuhpels) are like lists except for one main thing.

Tuples are **immutable**. Immutable means you can't change it.
This is just means, simply, that you can't change the things inside
of a tuple.

```python
some_tuple = (1, 2, 3, 4, 5, 6)

some_tuple[0] # -> 1
```

Because tuples are immutable, you might think that this
is a disadvantage. But, because they're immutable, they
actually have a performance benefit.

### Images and Tuples

The basic unit of measurement in images is the pixel. A pixel's
information is stored in a tuple (3-tuple, a tuple of three values).

The 3-tuple tells us for ONE PIXEL, what the RED, GREEN,
and BLUE values are.

```
			r    g    b
RED =    (255,   0,   0)
GREEN =  (  0, 255,   0)
BLUE =   (  0,   0, 255)
WHITE =  (255, 255, 255)
BLACK =  (  0,   0,   0)
GRAY =   (128, 128, 128)
```