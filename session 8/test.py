team= "new england patriots"

# def find(word, letter):
#     index=0
#     while index<len (word):
#         if word [index]== letter:
#             return index
#         index= index+1
#     return -1

# print (find (team, 'e'))

count=0
for letter in team:
    if letter =='a':
        count= count+1

print (count)
