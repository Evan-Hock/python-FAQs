# Mapping
## Map
The `map` function takes a function as its first parameter and an iterable as its second. It returns a new iterable where every element in the old iterable
has been passed through the function. It is also variadic: it takes multiple iterables, in which case the iterables will be harvested to supply
arguments to the function.\
`map` is equivalent to Haskell's `map` function when it is used with a single iterable, or `zipWithN` when used with N iterables.\
It can be thought of as this generator:
```py
def map(f, *xs):
    for pairing in zip(xs):
        yield f(*pairing)
```
## Starmap
`itertools.starmap` is like `map`, but it only accepts one iterable, and the elements from the iterable are each unpacked into its function.
```py
def starmap(f, xs):
    for args in xs:
        yield f(*args)
```
