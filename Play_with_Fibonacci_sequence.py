def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = int(input())

# check if the number of terms is valid

   #print("Fibonacci sequence:")
for i in range(nterms):
   print(recur_fibo(i),end=" ")