# Zip
`zip`, given a number of iterables, returns an iterable of tuples where each tuple consists of elements from its index in the original iterables.\
`zip` is a lazy function: if one of its iterables is short, all the iterables will be cut to that length.
```py
print(*zip(['a', 'b', 'c'], [97, 98, 99], [1, 2, 3, 4]) # -> ('a', 97, 1) ('b', 98, 2), ('c', 99, 3)
```
Barring types, `zip` is its own inverse:\
`zip(*zip(*xs))` = `xs`
