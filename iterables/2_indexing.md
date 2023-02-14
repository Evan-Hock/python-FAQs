# Indexing
Unlike most programming languages, Python supports negative indexing. Negative indexing starts from the back of the array.
```py
xs = range(10)
print(xs[-1]) # -> 9
print(xs[-10]) # -> 0
```
This is not exactly modular indexing. The only valid indices `i` for an arbitrary array `xs` are `-len(xs) ≤ i < len(xs)`.
# Next
[slicing](2a_slicing.md)
[mutations](3_mutations.md)
