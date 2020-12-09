"""Project Euler Problem 5 by Teddy Tortorici
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def find_factors(x):
    """outputs a list of the factors of x, if factors is empty, then x is prime"""
    factors = [0] * int(x+1)
    x = float(x)
    for divisor in range(2, int(x+1)):
        while True:
            if x/divisor == int(x/divisor):
                x /= divisor
                factors[divisor] += 1
            else:
                break
    return factors


def find_smallest_evenly_divisible(n):
    """returns the smallest number that is evenly divisible by all the numbers from 1 to n"""
    factors_list = [0] * int(n)
    # will fill this with exponents ignoring first two terms [0, 0, a, b, c, ...] corresponds to 2^a * 3^b * 4^c * ...
    # sum over each number between 1 and n in reverse order
    for num in range(n)[::-1]:
        factors = find_factors(num)
        for ii, f in enumerate(factors):
            # If there are more factors, include them, if not, they are already accounted for
            if f > factors_list[ii]:
                factors_list[ii] = f
    # now we want to create the product
    product = 1
    for ii in range(2, n):
        product *= ii ** factors_list[ii]
    return product


if __name__ == '__main__':
    print(find_smallest_evenly_divisible(10))
    print(find_smallest_evenly_divisible(20))


'''import numpy as np
import copy

def LCM_simple(L):
## an inefficient function that finds the smallest multiple of all numbers in list 'L'
  try:
    L.remove(1)
  except:
    pass
  L0 = copy.copy(L)
  L = np.array(L)
  while sum(np.abs(np.abs(L[1:])-np.abs(L[:-1]))) != 0:
    n = np.argmin(L)
    L[n] = L[n]+L0[n]
  if L[0] == L[-1]:
    return L[0]
  else:
    return 'I have failed you'

def GCD_simple(A,B):
## an inefficient function that finds the GCD of two numbers
  if A == B:
    return A
  elif A > B:
    R = int(A/2)+1
    S = B
    if R < S:
      return 1
  else:
    R = int(B/2)+1
    S = A
    if R < S:
      return 1
  for r in np.arange(S,R)[::-1]:
    if A%r == 0 and B%r == 0:
      return r
      break
  return 1

def GCD(A,B):
## find the GCD using euclidian alg
  r = True
  a = int(A)
  b = int(B)
  while r:
    q = a/b # quotient
    r = a%b # remainder
    if r:
      a = b
      b = r
    else:
      return b

def LCM(A,B):
## find LCM using 
  lcm = abs(A*B)/GCD(A,B)
  return lcm

def LCM_list(L):
  try:
    L.remove(1)
  except:
    pass
  lcm_old = copy.copy(L)
  while len(lcm_old) != 1:
    lcm_new = []
    for a,b in zip(lcm_old[0::2],lcm_old[1::2]):
      lcm_new.append(LCM(a,b))
    if len(lcm_old)%2:
      lcm_new.append(lcm_old[-1])
    lcm_old = copy.copy(lcm_new)
  return lcm_old
  
if __name__ == '__main__':
  print LCM_list(range(1,21))
'''