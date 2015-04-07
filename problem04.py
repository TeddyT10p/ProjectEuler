import numpy as np

def lpp(n):
  ## find the largest palindrome product of 2 n-digit numbers
  k = 10**(n-1)
  K = range(k,k*10)[::-1]
  plist = []
  for x in K:
    for y in K:
      if x == y:
        break
      prod = x*y
      if str(prod) == str(prod)[::-1]:
        plist.append(prod)
  plist = np.array(plist)
  return np.amax(plist)

if __name__ == '__main__':
  print lpp(3)
