from math import *  # * wild card
from random import randrange  # imports individual functions, classes variables ect.
import my_import

# Functions
square = 1
# you can't change globals locally

def my_function(name = "Zoe"):
    '''
    says hello
    :param name:
    :return: none
    '''
    print("Hello", name) # this will always run on excution or import
    print("square =", square)



my_function("Zoe")


def square_cube(n):
    '''
    returns square and cube of the number
    :param n:
    :return: square, cube
    '''
    square = n ** 2
    cube = n ** 3
    my_import.product_sum(square, cube)
    print("square =", square)
    return square, cube


if __name__ == "__main__":
    # this is the file that your executed/ran
    my_function("Zoe")
    my_import.product_sum(10, 20)
    print(randrange(100))
    print(pi)
    print(square_cube(7))
    sqr_cube = square_cube(7)
    print(sqr_cube[0], sqr_cube[1])
    sqr, cube = square_cube(8)
    print(sqr, cube)

# scope rules
# python (__main__), global (far left), local (inside functions or methods)
# you can see a global variable any where but you can't change it locally
# you can only change a local variable locally.  local variables do not exist outside of their name space

    my_function(name = "Zoe")
    my_function()

    print("Hello", "World", end = " ", sep = "")
    print("World")
