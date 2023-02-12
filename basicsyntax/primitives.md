# Primitive data types
Python features a few primitive data types:
* `int`: Unlimited precision, unbounded integers. `1`, `2`, `10`
* `float`: Familiar IEEE-754 floating point numbers. `0.5`, `float('inf')`, `float('nan')`
* `complex`: Complex numbers. `1j`, `-1 + 0j`, `1+1j`, `complex('inf')`
* `bool`: `True` and `False`. Considered a subtype of `int`
* `None`: A singleton to represent the absence of a value
* `str`: A sequence of characters. Both `"` and `'` may be used, as long as they are consistent. Python makes no distinction between a `chr` and a `str`

# More on strings
There are special string literals that can be used by prefixing a normal string with a letter:
* Format strings begin with f or F followed immediately by a normal string. they can contain expressions within curly brackets `{}` that will be
    evaluated at runtime and inserted into the string. `f'1 + 1 = {1 + 1}'` will be converted into `'1 + 1 = 2'` at runtime.
* Raw strings begin with r or R followed immediately by a normal string. Normal python strings can contain escape sequences, i.e. \n (newline),
    \t (horizontal tab), \r (carriage return), \x17 (end of transmission block), \u03c0 (π).\
    In raw strings, these escape sequences will be interpreted literally. Notably, however, raw strings cannot end with a backslash,
    because the way raw strings are interpreted Python will think that the closing quote on the string is part of the raw string.\
    To illustrate the difference between raw strings and normal strings:\
    `print('\u3c0')` → π\
    `print(r'\u3c0')` → \u3c0

Next part: [operators](operators.md)
