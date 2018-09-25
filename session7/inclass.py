# a = 4
# x = 3
# y = (x + a/x) / 2
# print(y)

# x = y
# y = (x + a/x) / 2
# print(y)

# x = y
# y = (x + a/x) / 2
# print(y)

# x = y
# y = (x + a/x) / 2
# print(y)

# x = y
# y = (x + a/x) / 2
# print(y)

# x = y
# y = (x + a/x) / 2
# print(y)

# while True:
#     print(x)
#     y = (x + a/x) / 2
#     if abs(y-x) < 0.0000001:
#         break
#     x = y

# def countdown(n):
#     while n > 0:
#         print(n)
#         time.sleep (2)
#         n = n - 1
#     print('Blastoff!')

# countdown(5)

import math

def mysqrt(a):
    x=3
    while True:
        print(x)
        y = (x + a/x) / 2
        if abs(y-x) < 0.0000001:
            break
        x = y

# print(mysqrt(9))

def libmath(a):
    return math.sqrt(a)
# print(libmath(9))

for i in range (1,10):
    print (i)
    print (mysqrt(i))
    print (libmath(i))
    print (abs ((float mysqrt (i))- libmath(i)))



# def printout():
#     for i in range (1,8):
#         i= float (i)
#         a= mysqrt(a)
#         l= libmath(a)
#         print (i, a, l, abs(a-l))

# printout()