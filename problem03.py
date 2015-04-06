import numpy as np

def prime_gen(x):
  ## a function that generates a list of prime numbers up to 'x' in accending order
  p_list = [2,3,5]
  n_list = range(2,int(x))
  n_check = linspace(0,0,len(n_list))
  r0 = [1,13,17,29,37,41,49,53]
  r1 = [7,19,31,43]
  r2 = [11,23,47,59]
  for n,i in zip(n_list,range(len(n_list))):
    if n%60 in r0:
      
    elif n%60 in r1:
    
    elif n%60 in r2:

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
