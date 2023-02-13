# Indexing
Unlike most programming languages, Python supports negative indexing. Negative indexing starts from the back of the array.
```py
xs = range(10)
print(xs[-1]) # -> 9
print(xs[-10]) # -> 0
```
This is not exactly modular indexing. The only valid indices `i` for an arbitrary array `xs` are `-len(xs) ≤ i < len(xs)`.

# Slicing
Given that `xs` is a sequence that supports slicing,\
`xs[<start index>:<stop index>:<step amount>]` will return a "slice" of xs starting at start, incrementing by step, and stopping just below (not at) stop.\
Some of these have default values if left out:
* If start is ommitted, it defaults to `0`, or, if step is negative, to `-1`.
* If stop is ommitted, it defaults to `len(xs)` (the end of the array), or, if step is negative, to `-len(xs) - 1`.
* If step is ommitted, it defaults to `1`. The second colon is optional if step is ommitted.
Slicing does two main things:
1. It returns a copy of the collection, but
2. When used as the left argument of an assignment, it mutates the values at those indices in the original array.
    The value on the right side must be of equal length to the slice.

Example:
```py
xs = list(range(10))
print(xs[5:]) # -> [5, 6, 7, 8, 9]
print(xs[::-1]) # -> [9, 8, 7, 6, 5, 4, 3, 2, 1]
xs[::2] *= [0] * 2
print(xs) # -> [0, 1, 0, 3, 0, 5, 0, 7, 0, 9]
print(list(filter(lambda x: x > 0, xs))) # -> [1, 3, 5, 7, 9]
```
