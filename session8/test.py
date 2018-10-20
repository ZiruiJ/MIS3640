# team= "New england patriots"

# def find(word, letter):
#     index=0
#     while index<len (word):
#         if word [index]== letter:
#             return index
#         index= index+1
#     return -1

# print (find (team, 'e'))

# count=0
# for letter in team:
#     if letter =='a':
#         count= count+1

# print (count)


'''Encapsulate this code in a function named count, and generalize it so that 
it accepts the string and the letter as arguments.'''

# def count (s, letter):
#     count= 0
#     for each in s:
#         if each == letter:
#             count= count+1
#     return count

# print (count (team, 'n'))

# new_team= team.upper()
# print (new_team)

# n= team.find('a')
# # print (n )
# print(team.find('en'))

# print(team.find('a', 10))
'''question print(team.find('a', 10)) 
# Read the documentation of this function to find out
# what it does.
# https://docs.python.org/3/library/stdtypes.html#str.find
# find(sub[, start[, end]])'''

name = 'bob'
print(name.find('b', 1, 3))

