def fibo(n):

   if n <= 1:
       return n
   else:
       return fibo(n-1) + fibo(n-2)
term=7

if term <= 0:
     print("Plese enter a positive integer")
else:
     print("Fibonacci sequence:")
for i in range(term):
       print(fibo(i))