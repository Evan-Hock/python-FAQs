# Sorted
`sorted(xs, /, *, key=None, reverse=False)` returns a sorted list consisting of the elements from `xs` after they have been passed through `key`.
If `reverse` is `True`, the ordering will be inverted.
```py
print(sorted([3, 1, 10, 9, 2], key=str, reverse=True)) # -> [9, 3, 2, 10, 1]
```
