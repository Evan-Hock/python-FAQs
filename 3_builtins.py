# Be sure to read basicsyntax.py first

####################
# import statements
####################

# they dont have to go at the beginning of the file (but it is convention)
import functools as ft # the functools namespace is now renamed to 'ft' for this file, so functools exports can be called with 'ft', i.e. 'ft.partial'
# the 'as' clause is not mandatory
# using a 'from ... import' statement allows you to import some number of exports from a particular module, e.g.
# from functools import reduce
# all names imported this way are put into the 'global namespace'
# the above import would import the reduce function from the functools module, and it would be usable as 'reduce' instead of 'functools.reduce'


##############
# any and all
##############

# these functions act on lists of bools
# any returns True if any of the values in its argument iterable are true
print(any([False, True, False])) # -> True

# all returns True if and only if all of the values in its argument iterable are true
print(all([False, True, False])) # -> False

# these functions can be thought of as a reduction by either the `or` operator (for `any`) or `and` operator (for `all`),
# with an initial value of either `False` (for `any`) or `True` (for `all`)
# this is a hint at the power of monoids
# the below definitions are semantically equivalent to the standard definitions
any = lambda xs: ft.reduce(lambda p, q: p or q, xs, False)
all = lambda xs: ft.reduce(lambda p, q: p and q, xs, True)


################
# enumerate(xs)
################

# enumerate takes a seq and returns it as a list of tuples of index, value pairs. it takes an optional 'start' parameter (which is 0 by default)
for i, x in enumerate(map(chr, range(97, 123)), 1):
    print(i, x, sep=': ', end=', ' if i < 26 else '\n')

print()
# STDOUT: (note: input is all on one line in reality)
# 1: a, 2: b, 3: c, 4: d, 5: e, 6: f, 7: g, 8: h, 9: i, 10: j,
# 11: k, 12: l, 13: m, 14: n, 15: o, 16: p, 17: q, 18: r, 19: s,
# 20: t, 21: u, 22: v, 23: w, 24: x, 25: y, 26: z


################
# filter(p, xs)
################

# filter returns only the elements from xs for which the unary predicate p returns true
# filter returns the objects in a special 'filter' iterable, not a list or any other built-in type. like other generators, it is consumed when used
print(*filter(lambda x: x % 2 == 0, range(10))) # -> 0 2 4 6 8
print(*filter(lambda x: x == abs(x), range(-5, 6))) # -> 0 1 2 3 4 5


########################
# iterable constructors
########################

# list, tuple, dict, and set functions all exist to construct their respective type

# set will convert the iterable so that it conforms to the rules for a set (no duplicate elements)
# additionally, because a set is unordered, there is no guarantee that the order will be maintained
# in fact, set will put the elements into sorted order, i.e. list(set([1, 5, 2, 1, 7, 2, 9])) -> [1, 2, 5, 7, 9]


##########
# len(xs)
##########

# len returns the length of a sequence
print(len([1, 2, 3])) # -> 3


######
# map
######

# map takes a function 'f' and a variable number of iterables and returns a new iterable (a map object) where each
# element is equal to the function 'f' called with arguments taken from each of the iterables in order
# map is lazy, so if any iterable in its input is longer than the others, its extraneous elements will be ignored
# note that because map produces a special 'map' generator object, its return value will be consumed (essentially destroyed) whenever it is used
print(*map(lambda x: x + 1, [1, 2, 3])) # -> 2 3 4
print(*map(op.mul, [1, 2, 3], [1, 2, 3])) # -> 1 4 9

##############
# max and min
##############

# these functions take a variable number of arguments or a single iterable and return the largest element among the argument list (or iterable)
# max and min both feature a keyword-only parameter called `key` that expects a unary function to filter the elements through
# to get a value to then compare them with each other
max([1, 2, 3]) # -> 3
min(*[1, 2, 3]) # -> 1, because min(*[1, 2, 3]) is equivalent to the call min(1, 2, 3)
max(1, 2, 3, key=op.neg) # -> 1, because max(1, 2, 3, key=op.neg) = max(-1, -2, -3)


#######################
# numeric constructors
#######################

# int and float will attempt to convert their argument into an integer or float respectively
# i.e.
print(float('inf')) # -> inf (infinity)
print(int(3.4)) # -> 3
print(int('1010', 2)) # -> 10


########
# range
########

print(*range(10)) # range(x) returns an ascending contiguous sequence of numbers from 0 to just under x
# STDOUT:
# 0 1 2 3 4 5 6 7 8 9

print(*range(11, -1, -2)) # range(start, stop, step=1) returns a sequence beginning at start, stopping at just under (or above) stop, and changing by step
# STDOUT:
# 11 9 7 5 3 1


###############
# reversed(xs)
###############

# returns a reversed iterator of 'xs'. note that because it just returns an iterator this function has constant (O(1)) time complexity
# also, because its value is a generator, it is consumed whenever it is used
# to reverse a reversible sequence in place, use the reverse method (xs.reverse())
# to get a truly new reversed sequence out of another sequence, use the xs[::-1] idiom or a sequence constructor with reversed
print(*reversed(range(10)))
# STDOUT:
# 9 8 7 6 5 4 3 2 1 0


###################################################
# sorted(xs, /, *, key=lambda x: x, reverse=False)
###################################################

# sorted takes an iterable and returns its values in sorted order as a list (built-in type)
# sorted is guaranteed to be stable, which means that the relative order of equal elements will not be changed
# if key is provided, the values will be passed through it before they are compared to one another (the default is actually None, but the effect
# is equivalent to the identity function `lambda x: x`)
# if reverse is set to True, the iterable will be sorted in reverse order
# for in-place sorting of a list that modifies it as a side-effect, use the list's sort method (xs.sort())

print(*sorted([10, 2, 5, 3, 6, 1, 11, 20, 89, 8, 12, 9, 7], key=str)) # -> 1 10 11 12 2 20 3 5 6 7 8 89 9 (Javascript sort)


##########
# sum(xs)
##########

print(sum([1, 2, 3])) # sum specifically takes an iterable
# STDOUT:
# 6

print(sum([1, 2, 3], start=1)) # it also takes an optional `start` argument
# STDOUT:
# 7

# also remember that for any finite arithmetic sequence, the sum equals (n / 2) * (2 * a1 + (n - 1) * d) or (n / 2) * (a1 + an), where
# n is the number of terms
# a1 is the first term of the sequence
# d is the common difference
# an is the last term of the sequence


######
# zip
######

# takes in a variable number of input iterators and returns a 'zip' generator object
# takes an optional `strict` parameter that when True will throw an exception if one of the iterables is short, otherwise, will consume them
# lazily, truncating the output to the shortest of the iterables
# "zips" together the input iterables into a sequence of tuples, where each tuple consists of elements that had a common index in the original
# set of iterables
# essentially, it performs matrix transposition
# zip is its own inverse with the star operator

print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))) # -> [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
print(list(zip(*[(1, 4, 7), (2, 5, 8), (3, 6, 9)]))) # -> [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
