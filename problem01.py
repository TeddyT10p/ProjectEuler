def mult_func(a,b,x):
  mult0 = range(a,x,a)
  mult1 = range(b,x,b)
  mult3 = range(a*b,x,a*b)
  return sum(mult0)+sum(mult1)-sum(mult3)

print mult_func(3,5,10)
print mult_func(3,5,1000)
