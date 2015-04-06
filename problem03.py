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
    if sieve[x]:
      for y in range(x**2,N+1,x**2):
        sieve[y] = False

  while True:
    try:
      p_list.append(n_list[0])
      n_list = [p for p in n_list if p%n_list[0]!=0]
    except:
      break
  return p_list
    
def LPF_find(n,prime_list):
  ## a function that finds the largest prime factor of 'n'
  primes = prime_gen(n/2)[::-1]
  print 'primes generated'
  for p in primes:
    if n%p == 0:
      lpf = p
      break
  try:
    return p
  except:
    print 'could not find any prime factors'
    return float('NaN')
n=600851475143.
p_list = prime_gen(n/2)
print LPF_find(n,p_list)
