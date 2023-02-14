# Keywords
Certain functions take keyword arguments, which can be provided with `<name>=<value>` syntax in the function parameters.
```py
xs = list(range(19, -1, -1))
xs.sort(key=str)
print(*xs, sep=', ', end=' This is JavaScript sort\n') # 0, 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 3, 4, 5, 6, 7, 8, 9  This is JavaScript sort
```

# Positional-only and keyword-only arguments
```py
def f(positional_only, /, normal, *, keyword_only):
    pass
```
By default for user-defined functions, all parameters can be provided either positionally or using the keyword syntax.\
To specify that certain parameters be provided positionally only, add a parameter `/` to the list between the parameter(s) you would like
to make positional-only and the rest of the parameters. For keyword-only parameters, add a `*`. This is the same `*` as in variadic functions
but without a name (as in variadic functions, the parameters listed after the variadic parameter are by nature keyword-only).

# Next
[control structures](5_controlstructures.md)
