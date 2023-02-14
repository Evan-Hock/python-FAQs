# Variadic functions
Functions that take a variable number of arguments can be denoted with the `*` syntax.\
Inside of the function, all of the variadic arguments will be collected into a tuple with the name given to the `*`'d parameter.
```py
def varargs_test(*xs):
    return type(xs)
    
print(varargs_test(1, 2, 3)) # <class 'tuple'>
```
```py
def make_tuple(*xs):
    return xs
    
print(make_tuple(1, 2, 3)) # (1, 2, 3)
```
```py
import functools as ft

def my_max(*xs):
    return ft.reduce(lambda x, y: x if y <= x else y, xs)
    
print(my_max(2, 1, 3)) # 3
```

# Next
[more syntax in functions](4c_extrafunctionsyntax.md)\
[control structures](5_controlstructures.md)
