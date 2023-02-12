# Primitive data types
Python features a few primitive data types:
* `int`: Unlimited precision, unbounded integers. `1`, `2`, `10`
* `float`: Familiar IEEE-754 floating point numbers. `0.5`, `float('inf')`, `float('nan')`
* `complex`: Complex numbers. `1j`, `-1 + 0j`, `1+1j`, `complex('inf')`
* `bool`: `True` and `False`. Considered a subtype of `int`
* `None`: A singleton to represent the absence of a value
* `str`: An immutable sequence of characters. Both `"` and `'` may be used, as long as they are consistent. Python makes no distinction between a `chr` and a `str`
* `list`: A mutable heterogenous list of objects: `[1, 2, 3]`, `[1, True, 'a']`
* `dict`: Key-value pairs: `{'a': 1, 'b': 2}`, `{}`
* `set`: Unique objects: `{1, 2, 3}`, `{False, 1, 'a'}`. The empty set can only be created with `set()`.
* `tuple`: Lists, but immutable: `1, 2, 3`, `4,`. Parentheses may be used, but are optional in certain contexts.

## Next
[more on strings](2a_strings.md)\
[operators](3_operators.md)
