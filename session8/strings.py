# team = 'New England Patriots'
# letter = team[1]  #The expression in brackets is called an index. 
# print(letter)

# #last letter
# last = team[len(team)-1]
# print(last)

'''ducks'''
# prefixes = 'JKLMNOPQ'
# suffix = 'ack'
# for letter in prefixes:
#     if letter == "O" or letter=="Q":
#         print (letter + 'u'+ suffix)
#     else:
        # print(letter + suffix)

team = 'New England Patriots'
# print (team[0:3])  #0 inclusive, 3 not inclusive "new"
# print(team[0:11])
# print (team [:11]) #==20
# print(team[12:20]) #== team [12:]

# print (team [11:4])  #ans: space there is no index 4 after 11

# print(team [::2])
# print (team[::-2])
# print (team [0:20:2])

# '''immutable'''
# new_team = team[:12]+'Seahawks'
# print(new_team)

# print (team)

# def find(word, letter):
#     index = 0
#     while index < len(word):
#         if word[index] == letter:
#             return index
#         index = index + 1
#     return -1
# print(find(team, 'a'))

'''for loop'''
# for i, letter in enumerate (team):
#     print (i, letter)


word = 'New England Patriots'
# count = 0
# for letter in word:
#     if letter == 'a':
#         count = count + 1
# print(count)

#理解？ Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.
# def count (s, letter):
#     c= 0
#     for each in s:
#         if each == letter:
#             c= c +1   #c+=1
#     return c

# print (count (team, 'a'))
# print (count (team, ' '))

# team = 'New England Patriots'
# new_team = team.upper()
# print(new_team)

team.split ('a')

s= '          a        '
