# Comprehensions
## List
`[<expr> for <identifier> in <sequence>]`
```py
print([x * x for x in [1, 2, 3]]) # -> [1, 4, 9]
```

## Dict
`{<key expr>: <val expr> for <identifier> in <sequence>}`
```py
print({k: v for k, v in zip(['ア', 'カ', 'タ'], ['a', 'ka', 'ta'])}) # -> {'ア': 'a', 'カ': 'ka', 'タ': 'ta'}
```
  
## Set & Generator
Syntax is same as for a list, but set comprehensions use `{}` and generator uses `()`. The parentheses on a generator comprehension can be removed
when it is the only argument to a function that expects an iterable.

## Multiple generators
Comprehensions can use multiple generators (`for ... in` expressions), in which case the rightmost ones produce elements faster.

They can also use conditions:
```py
print([x, y for x in range(-1, 2) for y in range(-1, 2) if x != 0 or y != 0])
```
output: `[(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]`

# Next
[indexing & slicing](2_indexingslicing.md)
