# Looping constructs
`for x in iter` will take elements from the iterator `iter` and bind them to the name `x`.\
It will do whatever is in its body with each `x` from `iter`.
```py
for x in range(1, 4):
    print(x, end=' ')
else:
    print()
```
The above code prints `1 2 3 4`.

Python loops can also have an `else` clause, which will execute if and only if the loop did not encounter a `break` statement.

```py
while True:
    print("Executed once")
    break
else:
    print("This will never execute")
```
This prints `Executed once`.

Python also has a `continue` keyword for its loops.
```py
for x in [1, 2, 3]:
    if x % 2 == 0:
        continue
    print(x, end=' ')
else:
    print()
```
The output from this one is `1 3`.
