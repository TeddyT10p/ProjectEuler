"""Project Euler Problem 1 by Teddy Tortorici
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""


def mult_func(a, b, x):
    mult0 = range(a, x, a)
    mult1 = range(b, x, b)
    mult3 = range(a * b, x, a * b)
    return sum(mult0) + sum(mult1) - sum(mult3)


if __name__ == "__main__":
    print(mult_func(3, 5, 10))
    print(mult_func(3, 5, 1000))
