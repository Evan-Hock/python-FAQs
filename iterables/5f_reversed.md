# Reversed
This function returns a *reversed iterator* out of its input. It does not actually reverse the sequence like the `reverse` method or the `xs[::-1]` idiom.\
Therefore, it has $O(1)$ time complexity.
```py
from itertools import accumulate
print(*accumulate(range(10))) # -> 0 1 3 6 10 15 21 28 36 45
print(*accumulate(reversed(range(10)))) # -> 9 17 24 30 35 39 42 44 45 45
```
