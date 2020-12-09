"""Project Euler Problem 3 by Teddy Tortorici
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""


def prime_gen(N):
    ## a function that generates a list of prime numbers up to 'x' in accending order
    p_list = [2, 3, 5]
    check = [False] * (N + 1)
    r0 = [1, 13, 17, 29, 37, 41, 49, 53]
    r1 = [7, 19, 31, 43]
    r2 = [11, 23, 47, 59]
    k = range(1, int(N ** 0.5) + 1)
    for x in k:
        for y in k:
            n = 4*x**2+y**2
            if n <= N and n % 60 in r0:
                check[n] = not check[n]
            n = 3 * x ** 2 + y ** 2
            if n <= N and n % 60 in r1:
                check[n] = not check[n]
            n = 3 * x ** 2 - y ** 2
            if n <= N and x > y and n % 60 in r2:
                check[n] = not check[n]
    for x in range(5, int(N ** 0.5)):
        if check[x]:
            for y in range(x ** 2, N+1 , x ** 2):
                check[y] = False
    for p in range(7, N):
        if check[p]:
            p_list.append(p)
    return p_list


def LPF_find(N):
    ## a function that finds the largest prime factor of 'n'
    primes = prime_gen(int(N**0.5))[::-1]
    print('primes generated')
    for p in primes:
        if N%p == 0:
            lpf = p
            break
    try:
        return lpf
    except:
        print('could not find any prime factors')
        return float('NaN')


if __name__ == '__main__':
  N = 600851475143
  print(LPF_find(N))
