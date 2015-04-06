import time

def prime_gen(x):
  ## a function that generates a list of prime numbers up to 'x' in decending order
  time_i = time.time()
  p_list = range(2,x,1)
  p_used = []
  i = -1
  while:
    i = i+1
    p_used.append(p_list[i])
    p_list = [p for p in p_list if p%p_list[i]==0]
    
  print 'generated primes in %d seconds'%(time.time()-time_i)
  return primes[::-1].append(2)

def LPF_find(n=13195):
  ## a function that finds the largest prime factor of 'n'
  primes = prime_gen(n/2)
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
time_i = time.time()
print LPF_find()
time_f = time.time()
print 'elapsed time is %d seconds'%(time_f-time_i)
