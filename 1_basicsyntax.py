#!/usr/bin/env python
# This is a comment
# The thing at the top of this is an example shebang: python is a scripting language,
# so while it's not strictly necessary it might help the interpreter find specifically which
# python version you want to use
"""
Multiline comments
look like this
"""

"""
In this document, whenever there is a print statement, it will be followed
by a comment saying "STDOUT:" with the output written verbatim on a comment
immediately underneath.
"""


#################################
# some basic language primitives
#################################

"""
singleton elements:
None (kind of like NULL), True, False

characters and strings are the same internally

strings, tuples, numbers, booleans, None, etc. are all immutable data types

lists, dicts (hashmaps), sets, and functions are mutable

arithmetic operators:
(+) addition, (-) subtraction, (*) multiplication, (/) float division,
(%) modulo, (//) integer division, (**) exponent

boolean operators:
not, and, or

equality operators:
(==) equals, (!=) not equals

identity operator:
is: x is y will check if x and y refer to the same object in memory. the 'is' operator is the prefered way to check for singletons. [1] is [1] -> False! (because lists are mutable)

bitwise operators:
(&) and, (|) or, (^) xor, (~) not, (<<) left shift, (>>) arithmetic right shift (value will have 1s shifted in if it was negative)

tuple syntax: 1, 2, 3
    optional parentheses allowed: (1, 2, 3)
list syntax: [1, 2, 3]
set syntax: {1, 2, 3}
dict syntax: {'a': 1, 'b': 2, 'c': 3}

strings:
normal strings can use either single or double quotes (there is no difference as long as the quotes match)
format strings begin with f or F followed immediately by a normal string. they can contain expressions within curly brackets {} that will be
    evaluated at runtime and inserted into the string, e.g. print(f'1 + 1 = {1 + 1}') -> 1 + 1 = 2
raw strings begin with r or R followed immediately by a normal string. normal python strings can contain escape sequences, i.e. \n (newline),
    \t (horizontal tab), \r (carriage return), \x17 (end of transmission block), \u03c0 (π)
    in raw strings, these escape sequences will be interpreted literally. notably, however, raw strings cannot end with a backslash,
    because the way raw strings are interpreted Python will think that the closing quote on the string is part of the raw string
    the difference between raw strings and normal strings:
    print('\u03c0') -> π
    print(r'\u03c0') -> \u03c0
    
    Python's regex libraries HIGHLY recommend using raw strings to represent regex instead of normal strings, due to the high prevalence of
    backslashes in regexes. this has caused a sort of myth with novice Python programmers that raw strings are "regex strings"
"""


############
# functions
############

# function definition: return and parameter types are implied
def f(x):
    """This is a docstring.
    
    Docstrings are multiline comments appearing at the first line of a function body. They are used by the __doc__ attribute. They usually
    follow this format, with a brief description on the very first line, followed by a space, then a longer description, with the closing
    quotes indented on their own line. They are optional, but highly recommended
    """
    return x

def g(x, y):
    return x + y
    
# functions are first-class
# lambdas (anonymous functions) are declared with the 'lambda' keyword followed by a parameter list, colon, and then return value
def flip(f):
    return lambda x, y: f(y, x)

"""
the above is equivalent to
def flip(f):
    def g(x, y):
        return f(y, x)
    return g
"""

print(flip(g)("concatenation", "string ")) # g = lambda x, y: x + y as defined above

# STDOUT:
# string concatenation

# the above is also a nice demonstration of duck typing: strings support +, so strings are allowed for this function


###################################
# control structures: if and match
###################################

# `if` should be familiar
if False:
    print("I couldn't think of anything better")
elif False:
    print("This is pretty dumb")
else:
    print("if is to be used for side-effects")
    
# STDOUT:
# if is to be used for side-effects


# python after 3.10 also has 'match', much to guido van rossum's chagrin, which is
# a lot like rust's 'match', but for side-effects only
match list(range(21)):
    case []: # pattern matching!
        print("This will not execute in this instance, because list(range(21)) does not look like []")
    case [x, *xs]: # this will match in this case, binding `x` to the first element and the rest to `xs`
        print(f"The first element is {x}.")
        print("The rest of the elements are", end=' ')
        print(*xs, end=".\n")
    case _: # this is a default catch-all case. like haskell and rust, the convention is to use an _ for an unused binding
        print("In this instance it does not execute, because unlike C and Javascript cases do not fall through")

# STDOUT:
# The first element is 0.
# The rest of the elements are 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20.


# conditional assignment with 'if' and 'else'
def twoArityMax(x, y):
    # `x if x >= y else y` actually evaluates to a value here
    return x if x >= y else y

# can be chained
def threeArityMax(x, y, z):
    return x if x >= y and x >= z else y if y >= x and y >= z else z

print(twoArityMax(3, 4)) # -> 4
print(threeArityMax(7, 10, 2)) # -> 10

####################################
# looping constructs: for and while
####################################

# `for x in iter`'s behavior is to always take elements from the iterable `iter` and bind them to the name `x`.
# `range` will create an iterable that represents an arithmetic sequence.
# `for x in iter` typically does not touch the iterable `iter`, but if said iterable is a generator, it will be consumed, removing its elements.
for x in range(1, 4):
    print(x, end=' ')
else: # loops may have an `else` clause, which will execute if and only if the loop did not encounter a `break` statement
    print() # the default behavior of print() is to print a new line

# STDOUT:
# 1 2 3

while True:
    print("This will be printed one time")
    break
else:
    print("This will never print")

# STDOUT:
# This will be printed one time

# Python additionally has a `continue` statement for its loops, unlike some scripting languages
for x in [1, 2, 3]: 
    if x % 2 == 0:
        continue
    print(x, end=' ')
else:
    print()
    
# STDOUT:
# 1 3
