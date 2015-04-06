def fibonacci(a0,a1,x):
  # x is the number to which the Fibonacci sequence reaches
  # a0 is the first seed
  # a1 is the second seed
  seq = [a0, a1]
  next = 0
  while next < x:
    next = seq[-1]+seq[-2]
    seq.append(next)
  return seq
 
fib_seq = fibonacci(1,2,4e6)
sum = 0
for i in fib_seq:
  if i%2 == 0:
    sum = sum+i
print sum
