import numpy as np

def prime_gen(N):
  ## a function that generates a list of prime numbers up to 'x' in accending order
  p_list = [2,3,5]
  check = [False]*(N+1)
  r0 = [1,13,17,29,37,41,49,53]
  r1 = [7,19,31,43]
  r2 = [11,23,47,59]
  K = range(1, int(np.sqrt(N))+1)
  for x in K:
    for y in K:
      n = 4*x**2+y**2
      if n<=N and n%60 in r0:
        check[n] = not check[n]
      n = 3*x**2+y**2
      if n<=N and n%60 in r1:
        check[n] = not check[n]
      n = 3*x**2-y**2
      if n<=N and x>y and n%60 in r2:
        check[n] = not check[n]
  for x in range(5,int(np.sqrt(N))):
    if check[x]:
      for y in range(x**2,N+1,x**2):
        check[y] = False
  for p in range(7,N):
    if check[p]:
      p_list.append(p)
  return p_list
    
def LPF_find(N):
  ## a function that finds the largest prime factor of 'n'
  primes = prime_gen(int(np.sqrt(N)))[::-1]
  print 'primes generated'
  for p in primes:
    if N%p == 0:
      lpf = p
      break
  try:
    return lpf
  except:
    print 'could not find any prime factors'
    return float('NaN')

if __name__ == '__main__':
  N = 600851475143
  print LPF_find(N)
