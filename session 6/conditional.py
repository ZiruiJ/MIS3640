# age = input('Please enter your age:  ')

# if int(age) >= 18:  #int(age)to convert
#      print ('adult')
# elif int(age) >= 6:
#     print ('teengaer')
# else:
#     print('kid')  #the sequence is important, it will stop at the first criteria. check the logic. no error. 

# x= 18
# y=20
# if x==y:
#     print ('x and y are equal')
# else:
#     if x<y:
#         print ('x is less than y')
#     else:
#         print ('x is greater than y')


# weight= input ('Please enter your weight in kg:  ')
# height= input ('Please enter your height in m:  ')
# BMI= float(weight)/(float (height)**2)
# if float(BMI) <= 18.5:
#     print ('underweight')
# elif 18.5 <=float(BMI) < 24.9:
#     print ('normal weight')
# elif 25< float(BMI) <29.9:
#     print ('overweight')
# else:
#     print ('obesity')

#sample
# import webbrowser

# def calculate_bmi (weight, height):
#     bmi=703*weight /(height*height)
#     if bmi <= 18.5:
#         print ('your bmi is {:.1f}. You are underweighted.'. format (bmi))  #为什么format bmi
#         webbrowser.open
#         ('https://www.mcdonalds.com/us/en-us.html')

# def compare (varA, varB):
#     if isinstance(varA, str) or isinstance(varB, str) :
#         print ('string involved')
#     else:
#         if varA> varB:
#             print('bigger')
#         elif varA== varB:
#             print ('equal')
#         else:
#             print ('smaller')
    
# a='hello'
# b=3
# c=5
# compare (a,b)
# compare (b,c)

'''Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.'''

# def diff21(n):
#   if n <= 21:
#     return 21-n
#   else:
#     return (n-21)*2

# print(diff21(19))
    
'''When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, 
inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. 
Return True if the party with the given values is successful, or False otherwise.'''

# def cigar_party(cigars, is_weekend):
#     if is_weekend and cigars >=40:
#         return True
#     else: 
#         if 40<= cigars<=60:
#             return True
#         else:
#             return False

'''sample'''
# return 40<= cigars <=60 or is_weekend and cigars >= 40

# print (cigar_party(30, False))

'''recursion, need a way to stop itself'''
# def countdown(n):
#     if n <= 0:
#         print('Blastoff!')
#     else:
#         print(n)
#         countdown(n-1)
# countdown(3)

# def print_n(s, n):
#     if n <= 0:
#         return
#     print(s)
#     print_n(s, n-1)

# print_n ('hello', 3) 

# def fibonacci (n):
#     if n==1 or n==2:
#         return 1
#     return fibonacci(n-2)+fibonacci(n-1)

# print (fibonacci(4))

# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return fact(n-1)*n

# print (fact(4))

'''3/2= 1, 3%2=1*2+1 9%mod4=4*2+1 25%10=(10*2+5)= 5'''

print ('current a, b', a, b)
if b==0:
    return a
else: 
    return gcdRecur (b, a % b)
    


