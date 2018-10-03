fin = open("C:/Users/zjiao1/Desktop/MIS3640/session9/word.txt")

# line = fin.readline()
# word = line.strip()
# print(word)

# line = repr(fin.readline()) 
# print (line)

# line = fin.readline()
# word = line.strip()
# print(word)

counter = 0

for line in fin:
    word = line.strip()
    # print(word)
    counter+=1

print("total words:", counter)

def read_long_words():
    """
    prints only the words with more than 20 characters
    """
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word)

# read_long_words()

# def has_no_e(word):
#     """
#     returns True if the given word doesn’t have the letter “e” in it.
#     """
#     for letter in word:
#         # if letter == 'e' or letter=='E':
#         if letter.lower() == 'e':
#             return False
#     return True
# #     return not 'e' in word.lower()

# # print(has_no_e('Babson'))
# # print(has_no_e('College'))
# # print(has_no_e('Epslon'))

# def find_words_no_e ():
#     counter_no_e=0
#     counter_total= 0
#     for line in fin:
#         counter_total+=1
#         word= line.strip()
#         if has_no_e (word):
#             counter_no_e+=1
#     return counter_no_e/ counter_total

# print ('the percentage of the words with no "e" is {:.2f}%.' .format (find_words_no_e()*100))


def avoids(word, forbidden):
    """
    takes a word and a string of forbidden letters, and that returns True
    if the word doesn’t use any of the forbidden letters.
    """
    for letter in word:
        if letter in forbidden:
            return False
    return True


print(avoids('babson', 'def'))

# def find_words_no_vowels ():
#     counter_no_vowel=0
#     counter_total=0
#     for line in fin:
#         counter_total+=1
#         word= line.strip()
#         if avoids (word, 'aeiouy'):
#             print (word)
#             counter_no_vowel+=1
#     return counter_no_vowel/counter_total

# print ('the percentage of the words with vowel letter is {:.2f}%.'.format (find_words_no_vowels()*100))


# print(avoids('Babson', 'ab'))
# print(avoids('College', 'ab'))

# def uses_only(word, available):
#     """
#     takes a word and a string of letters, and that returns True if the word
#     contains only letters in the list.
#     """
#     for letter in word: 
#         if letter not in available:
#             return False
#     return True


# print(uses_only('Babson', 'aBbsonxyz'))
# print(uses_only('college', 'aBbsonxyz'))

# def uses_all(word, required):
#     """
#     takes a word and a string of required letters, and that returns True if
#     the word uses all the required letters at least once.
#     """
#     for letter in required: 
#         if letter not in word:
#             return False
#     return True


# print(uses_all('Babson', 'abs'))
# print(uses_all('college', 'abs'))

# def find_words_using_all_vowels():
#     counter= 0
#     for line in fin:
#         word= line.strip ()
#         if uses_all (word, 'aeiouy'):
#             print (word)
#             counter +=1
#     return counter
# print ('the number of words that use all the vowel:', find_words_using_all_vowels())

# def is_abecedarian(word):
#     """
#     returns True if the letters in a word appear in alphabetical order
#     (double letters are ok).
#     """
#     previous = word[0]         
#     for c in word:
#         if c < previous:
#             return False
#         previous = c
#     return True


# def find_abecedarian_words():
#     counter= 0
#     current_longest_word= ''
#     for line in fin:
#         word= line.strip ()
#         if is_abecedarian(word):
#             print (word)
#             counter +=1
#             if len(word) > len(current_longest_word):
#                 current_longest_word=word
#     return counter,current_longest_word

# print ('the number of words that is abecedarian:', find_abecedarian_words())


'''Rewrite is_abecedarian using recursion'''
def is_abecedarian_using_recursion (word):
    if len (word)<=1:
        return True
    if word[0]> word[1]:
        return False
    return is_abecedarian_using_recursion(word[1:])



print(is_abecedarian_using_recursion('abs'))
print(is_abecedarian_using_recursion('college'))


'''Rewrite is_abecedarian using while loop.'''

# def is_abecedarian(word):
#     i= word[0]
#     while i< word:
#         print (i)
#         i+= word[1]
#         return True
#     return False

# print(is_abecedarian('abs'))
# print(is_abecedarian('college'))


# def is_abecedarian_using_while(word):
#     """
#     returns True if the letters in a word appear in alphabetical order
#     (double letters are ok).
#     """
#     i = 0
#     while i < len(word)-1:
#         if word[i+1] < word[i:]:
#             return False
#         i = i + 1
#     return True

# print(is_abecedarian_using_while('abs'))
# print(is_abecedarian_using_while('college'))