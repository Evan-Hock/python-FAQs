# Control Stuctures
`if` should be familiar
 ```py
 if False:
    print("I couldn't think of anything better")
elif False:
    print("This is pretty dumb")
else:
    print("if is to be used for side-effects")
```
The above will print `if is to be used for side-effects` to the console.

Python after 3.10 also has `match`
```py
match list(range(21)):
    case []: # pattern matching!
        print("This will not execute in this instance, because list(range(21)) does not look like []")
    case [x, *xs]: # this will match in this case, binding `x` to the first element and the rest to `xs`
        print(f"The first element is {x}.")
        print("The rest of the elements are", *xs, end='.\n')
    case _: # this is a default catch-all case. like haskell and rust, the convention is to use an _ for an unused binding
        print("In this instance it does not execute, because unlike C and Javascript cases do not fall through")
```
The above will print
```
The first element is 0
The rest of the elements are 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20.
```
`if` and `else` can also be used for conditional assignment
```py
def threeArityMax(x, y, z):
    return x if x >= y and x >= z else y if y >= x and y >= z else 
```
