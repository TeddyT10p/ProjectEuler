"""Project Euler Problem 4 by Teddy Tortorici
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""


def lpp(n):
    """find the largest palindrome product of 2 n-digit numbers"""
    k = 10 ** (n-1)
    m = range(k, k * 10)
    palindromic = 0
    for x in m:
        for y in m:
            if x <= y:
                product = x * y
                if str(product) == str(product)[::-1] and len(str(product)) == 2*n and product > palindromic:
                    palindromic = product
                    # print('found next larger prod: {}'.format(product))
    return palindromic


if __name__ == '__main__':
    print(lpp(3))
