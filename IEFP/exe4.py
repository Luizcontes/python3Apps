a=0
b=1
for i in range(23):
   fib = a + b
   a = b
   b = fib
print(fib)