# MATH

# float: have decimals
# integers: are counting numbers (no decimals)

print(1.2 / 2 + 1.2)
# doesn't print 1.8 because floats operates differently, can result in floating point errors
my_float = 1.2 / 2 + 1.2
print(int(my_float))  # int() chops off the decimals

my_int = 123
print(my_int)
print(float(my_int)) # adds decimals

# Variables
snake_case = "lower case with underscores between words"
print(snake_case)

camelCase = "JavaScript uses this"

# the following things are not allowed
# my variable - spaces
# my_variable! - no special characters
# my.variable - no decimals
# 8ball - no numbers to start variable names
# ball8 - is fine though

# Assignment
my_variable = 8
x, y = (3, 4)
print(x)
print(y)

# Math Operators
# + - * /
# ** : exponents
# // : floor division, similar to int(), rounds down
# %  : modulo, remainder after division

# Compound Assignment Operators
# += -= *= /=
x = 5
x += 1  # equivalent of x = x + 1
print(x)

x *= 3  # same as x = x * 3
print(x)

x **= 0.5
print(x)

# Round
print(round(x, 3))

# Format "{}".format()
# for formatting TEXT

# formatting text as an example:
first = "Jerry"
last = "Garcia"
print(first, last)
print(first + last)

print("{}".format(first))
print("my name is {} {}.".format(first, last))

print("First: {} \n Last: {}".format(first, last))
print("First: {1} \n Last: {0}".format(first, last)) # allows you to chose which item goes where

# most of our formatting will be done with numbers
# you may specify d for digit/int, f for float, e for exponent to force a format

# round to three decimal places {:.3f}
pi = 3.14159265387
print("{:.3}".format(pi))

# add a sign to a number {:+}
# this works for positive and negative numbers (both use +)
print("{:+}".format(pi))

# add comma formattting to a number {:,}
my_number = 719273
print("{:,}".format(my_number))

# right align :>xd where x is the width of text
print("{:>20}".format(first))

# left align :<xd
print("{:<20}".format(first))

# center align :^xd
print("{:^20}".format(first))

# percent {:%} {:2%}
print("{:2%}".format(.234))

# exponent {:e}
print("{:e}".format(13213))

# leading 0s and other placeholders {:.05}
print("{:05}".format(234))  # the number after the 0 spesifies the number of places the whole number takes up

# dollars and cents
# 142.3 --- $142.3
print("${:.2f}".format(142.3))

# Github- Git is a VCS (Version Control System)
# allows you to go back to past changes and revert to or see old code


