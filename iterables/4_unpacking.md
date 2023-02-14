# Unpacking
You can unpack both sequences and dictionaries into functions and assignment statements.
## Sequences
```py
print(*[1, 2, 3]) # -> 1 2 3
```
## Dictionaries
```py
print(*[1, 2, 3], **{'sep': ', ', 'end': '.\n'}) # -> 1, 2, 3.
```
## Assignments
Tuple unpacking
```py
x, y, z = 1, 2, 3
print(x, y) # -> 1 2
```
Rest unpacking
```py
x, *y = 1, 2, 3
print(x, y) # -> 1 [2, 3]
print(type(y)) # -> <class 'list'>
```
A good rule of thumb is that when unpacking into a function, the `*` goes with the iterable, and when unpacking into an assignment, the `*` goes with
the rest lvalue on the left side.
