# Mutations
In this document, the variables `xs` and `ys` will reappear. They start with these states and mutate as the document goes along:
```py
xs = list(range(10)) # Reminder: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ys = list(range(10))
```
For a mutable, slicable collection `xs`, `xs.append(x)` is intended to be identical to `xs[len(xs):] = [x]`.
```py
xs.append(10)
ys[len(ys):] = [10]
```
After these operations, `xs` and `ys` are still equal.

To add a variable number of elements to the end of an array, use `extend`. `xs.extend(ys)` is equal in effect to `xs[len(xs):] = ys`.
```py
xs.extend(range(11, 21))
ys[len(ys):] = range(11, 21)
```
After these operations, `xs` and `ys` are still equal.

To remove elements, use `remove`.
```py
xs.remove(20)
del ys[ys.index(20)]
```

`pop` can be used to remove and return a value from the list. It takes an optional index as an argument, which, if unprovided, causes the
last element to be removed.
```py
print(xs.pop()) # 19
```

# Next
[variadic functions](4_variadics.md)
