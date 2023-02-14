## Filter
Filter takes a unary predicate (a function that takes a single value and returns a bool) and an iterator and returns an iterable containing only the
elements from its input iterator that the predicate returns `True` for.
```py
print(*filter(lambda x: x not in 'aeiou', 'This will remove all the vowels'), sep='')
```
`Ths wll rmv ll th vwls`
## Filter false
`itertools.filterfalse` is the opposite of `filter`.
```py
from itertools import filterfalse
print(*filterfalse(lambda x: x in 'aeiou', 'This will remove all the vowels'), sep='')
```
`Ths wll rmv ll th vwls`
