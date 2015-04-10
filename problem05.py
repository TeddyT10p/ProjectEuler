import numpy as np
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
