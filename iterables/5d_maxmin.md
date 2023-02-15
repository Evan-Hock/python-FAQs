# Max and min
`max` and `min` are both [variadic](../basicsyntax/4_variadics.md), but they also accept iterables:
```py
print(max([1, 3, 2])) # -> 3
```
```py
print(min([3, 2, 1])) # -> 1
```
They also both accept a keyword-only argument called `key`. `key` is a unary function: if it is provided, the arguments are passed through `key` before they are compared.
