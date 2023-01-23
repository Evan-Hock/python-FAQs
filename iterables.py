# Be sure to read basicsyntax.py first

##################
# basic iterables
##################

# list, denoted by []: mutable, non-hashable
print([1, 2, 3])
# STDOUT:
# [1, 2, 3]

# dict, denoted by {}, with key-value pairs defined by `key: value`
print({'a': 1, 'b': 2, 'c': 3}
# STDOUT:
# {'a': 1, 'b': 2, 'c': 3}
      
# set, denoted by {} and formatted much more like a list
# remember that the basic rules of mathematics say that sets cannot have duplicate elements!
# also, {} is an empty dict, not a set
print({1, 1, 1})
# STDOUT:
# {1}
      
# tuples, indicated by , and potentially () depending on context
# tuples are a lot like lists, but they are immutable
print((1, 2, 3))
# STDOUT:
# (1, 2, 3)


#################
# comprehensions
#################

# list: [<expr> for <identifier> in <seq>]
print([x * x for x in [1, 2, 3]])
# STDOUT:
# [1, 4, 9]

# set comprehension uses {}
# generator uses (), but the () is optional if the generator is passed in to a callable as the only argument

# dict comprehension
# {<key expr>: <val expr> for <identifier> in <seq>}
print({k: v for k, v in zip(['ア', 'カ', 'タ'], ['a', 'ka', 'ta'])})
# STDOUT:
# {'ア': 'a', 'カ': 'ka', 'タ': 'ta'}

# comprehensions can use multiple generators (`for ... in` expressions) in which case the rightmost ones produce elements faster
# they can also use conditions
print([x, y for x in range(-1, 2) for y in range(-1, 2) if x != 0 or y != 0])
# STDOUT:
# [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

#################
# seq operations
#################

xs = list(range(10)) # xs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# you probably knew about `for ... in`
# but you can also use `in` as an infix operator to check for set membership
print(10 in xs) # -> False
print(5 in xs) # -> True
print(10 not in xs) # -> True

# `in` also works for substrings
print('$' in '$100') # -> True

##########
# slicing
##########

# slice syntax
# xs[<start index>:<stop index>[:<step>]]
# the second colon is optional if there is no step
# if start index is ommitted, it is assumed to be 0
# if stop index is ommitted, it is assumed to be -1
# negative indices start from the back of the list and go in reverse, i.e. xs[-2] -> penultimate elem of xs
# if step is ommitted, it is assumed to be 1
# slicing does two things: it returns a copy of the collection, but when used as the left argument of an assignment, it mutates those indices in the original array

# xs previously defined as list(range(10))
print(xs[5:]) # -> [5, 6, 7, 8, 9]
print(xs[::-1]) # -> [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(xs[1::2]) # -> [1, 3, 5, 7, 9]

################
# seq unpacking
################

# as part of assignment...
# xs previously defined as list(range(10))
x, y = xs # Error! Too many values in xs
x, y = xs[-2:] # x = 8, y = 9
x, *y = xs # x = 0, y = xs[1:]

# unpacking a seq into a function
from random import randint
ys = ((randint(1, 6) for _ in range(10)) for _ in range(10))
zs = map(max, *ys)
# zs's value is unknowable at runtime but it's probably a sequence of 10 highly skewed values on a d6!
# map takes a variable list of seqs and a function with appropriate arity (max is variadic, however) so this will result in the maximum value out of all generated lists

print(*[1, 2, 3])
# STDOUT:
# 1 2 3

#####################
# variadic functions
#####################

# myfloatmax will appear to take any number of arguments
from functools import reduce
def myfloatmax(*xs):
    # xs is now a list in here
    return reduce(lambda x, y: x if y <= x else y, xs, -float('inf'))
# notice how the variadic syntax (*) mirrors the unpacking syntax

# positional-only and keyword-only arguments
# you can think of * as a varargs variable with no name (so it will absorb all positional arguments after a point)
def f(positional_only, /, normal, *, keyword_only):
    pass

# dictionary unpacking
# kwargs is just a dict in the function
def apply(f, *args, **kwargs):
    # *args will expand into any number of positional arguments into f, and
    # **kwargs will expand and match up to the keyword arguments of f
    return f(*args, **kwargs)
