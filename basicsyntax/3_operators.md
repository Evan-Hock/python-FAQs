# Operators
## Arithmetic
`+` addition, `-` subtraction, `*` multiplication, `/` float division, `%` modulo, `//` integer division, `**` exponentiation

## Boolean
`not`, `and`, `or`\
`x and y` is defined to be equivalent to the expression `x if not x else y`.\
`x or y` is defined to be equivalent to `x if x else y`.

## Equality
`==` and `!=`

## Comparison
`<`, `>`, `<=`, `>=`

## Bitwise
`&` and, `|` or, `^` xor, `~` not, `<<` left shift, `>>` arithmetic right shift

## Membership
`x in col` will return `True` if `x` is a member of the collection `col`.\
`x not in col` will return `True` if `x` is not a member of the collection `col`.

## Identity
`x is y` checks if x and y point to the same object in memory.\
`[1] is [1]` = `False` because `[1]` is a mutable list.\
`True is True` = `True` because there is only one `True` object.\
There is special syntax with `not`:\
`[1] is not [1]` = `True`

`is` is the preferred way to equality test with `None`.

# Next
[functions](4_functions.md)
