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
print(flip(lambda x, y: x + y)("concatenation, "string"))
```
Functions that take in a function and do something with it are called **higher-order functions**.\
Functions that take in a function as their only parameter, do something, and return a function are called decorators.
They are a subset of higher-order functions, and support the decorator syntax.\
As a silly example:
```py
def as_string(f):
    return lambda *args, **kwargs: str(f(*args, **kwargs))
  
@as_string
def jsAdd(x, y):
    return x + y
  
@as_string
def jsSub(x, y):
    return x - y

print(len(jsAdd(50, 50))) # 3
```
