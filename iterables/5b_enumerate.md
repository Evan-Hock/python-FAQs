## Enumerate
`enumerate(xs)` returns a list of index, value pairs of `xs`.
```py
for i, x in enumerate(map(lambda x: x ** 2, range(5))):
    print(i, x, sep=': ', end=', ' if i < 4 else '\n')
print()
```
The above outputs `0: 0, 1: 1, 2: 4, 3: 9, 4: 16`.
