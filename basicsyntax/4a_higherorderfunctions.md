# Higher Order Functions
Python functions are first-class, meaning they can be manipulated just like any other variable.\
The `lambda` keyword is used to declare an anonymous function (a function without a name).
```py
def flip(f):
    return lambda x, y: f(y, x)
```
The flip function above takes a function as its parameter and returns an arguments-reversed version
```py
# This code prints "string concatenation" using the above definition of `flip`
print(flip(lambda x, y: x + y)("concatenation", "string"))
```
**Higher-order functions** take in a function and do something with it.
If a higher-order function takes in a function as its only parameter and returns a function, python allows the decorator syntax to be used:
```py
@flip
def weird_sub(x, y):
    return x - y
```
is equivalent to
```py
def weird_sub(x, y):
    return x - y
    
weird_sub = flip(weird_sub)
```
# Next
[control structures](5_controlstructures.md)
