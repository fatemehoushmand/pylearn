fn = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0

if fn <= 0:
   print("Please enter a positive integer")

elif fn == 1:
   print("Fibonacci sequence upto",fn,":")
   print(n1)

else:
   while count < fn:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1