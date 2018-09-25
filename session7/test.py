import math
 
def newtons(n):
   x = n / 2 # rough estimate
   i = 0
   while i < 10:
       y = (x + n / x) / 2 # newtons method
       x = y
       i += 1
   return y
 
def libmath(n):
   return math.sqrt(n)
 
def printout():
   for i in range(1, 10):
       i = float(i)
       n = newtons(i)
       l = libmath(i)
       return i, n, l, abs(n-l)
 
printout()