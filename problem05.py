import numpy as np
import copy

def LCM_simple(L):
## a function that finds the smallest multiple of all numbers in list 'L'
  try:
    L.remove(1)
  except:
    pass
  L0 = copy.copy(L)
  L = np.array(L)
  while sum(np.abs(np.abs(L[1:])-np.abs(L[:-1]))) != 0:
    print L
    n = np.argmin(L)
    L[n] = L[n]+L0[n]
  if L[0] == L[-1]:
    return L[0]
  else:
    return 'I have failed you'

def GCD(A,B):
  if A > B:
    R = A
  else:
    R = B
  for r in range(2,R)[::-1]:
    if A%r == 0 and B%r == 0:
      gcd = r
      break
  return gcd

#def LCM(L):
  

if __name__ == '__main__':
  L = range(1,21)
  print LCM_simple(L)
