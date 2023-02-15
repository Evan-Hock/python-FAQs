# Any and all
`any` returns `True` if any of the values in its input iterable are `True`.\
`all` returns `True` if and only if all of the values in its input iterable are `True`.
```py
print(any(True, False, True)) # -> True
print(all(True, False, True)) # -> False
```
These functions can be thought of as a reduction:
```py
import functools as ft
any = lambda xs: ft.reduce(lambda p, q: p or q, xs, False)
all = lambda xs: ft.reduce(lambda p, q: p and q, xs, True)
```
