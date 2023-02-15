# Sorted
`sorted(xs, /, *, key=None, reverse=False)` returns a sorted list consisting of the elements from `xs` after they have been passed through `key`.
If `reverse` is `True`, the ordering will be inverted. If `key` is `None` (the default), the values will be compared as-is.
```py
print(sorted([3, 1, 10, 9, 2], key=str, reverse=True)) # -> [9, 3, 2, 10, 1]
```
```py
print(sorted(range(-10, 11), key=abs)) # -> [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10]
```
