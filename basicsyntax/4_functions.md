# Functions
Function definition: Types are implied.
```py
def identity(x):
    """This is a docstring.
    
    Docstrings are multiline comments appearing at the first line of a function body.
    They are used by the __doc__ attribute. They usually follow this format, with a brief description
    on the very first line, followed by a space, then a longer description, with the closing
    quotes indented on their own line. They are optional, but highly recommended.
    """
    return x # Return statements are the same as always
```
```py
def make_tuple(x, y):
    """This function returns a tuple containing x and y."""
    return x, y
```
## Next
[higher order functions](4a_higherorderfunctions.md)
[control structures](5_controlstructures.md)
