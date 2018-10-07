# names = ['Defne', 'Jack', 'Angela']
# scores = [95, 75, 85]
# grades = dict()
# grades ={'Defne': 90, 'Jack': 75, 'Angela': 85}
# print(grades)

# print(grades['Jack'])
# # print(grades['Sarah'])
# print (len(grades))

# def histogram (s):
#     d= dict()
#     for c in s:
#         if c not in d:
#             d[c]=1
#         else:
#             d[c]+=1
#     return d

# print (histogram('Bookkeeper'))

# h= histogram('Bookkeeper')
# num_of_e= h.get ('e',0)
# num_of_a= h.get ('a',0)
# print(num_of_a)
# print(num_of_e)

'''exercise 1'''
# released= 'bookeeper'
# count = {}
# for element in released:
#     count[element] = count.get(element, 0) + 1

# print (count)

# def print_hist(h):
#     for c in h:
#         print(c, h[c])
        
# h = histogram('Massachusetts')
# print_hist(h)

# for key in sorted (h):
#     print(key, h[key])

# def reverse_lookup(d, v):
#     for k in d:
#         if d[k] == v:
#             return k
#     raise LookupError()
# h = histogram('Massachusetts')
# key = reverse_lookup(h, 3)
# print(key)

# def invert_dict(d):
#     inverse = dict()
#     for key in d:
#         val = d[key]
#         if val not in inverse:
#             inverse[val] = [key]
#         else:
#             inverse[val].append(key)
#     return inverse

# hist= histogram('parrot')
# print(hist)

# inverse= invert_dict(hist)
# print(inverse)

# def fib(n):
#     global numFibCalls
#     numFibCalls += 1
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         return fib(n - 1) + fib(n - 2)


# known = {1: 1, 2: 2}


# def fib_efficient(n):
#     global numFibCalls
#     numFibCalls += 1
#     if n in known:
#         return known[n]
#     else:
#         ans = fib_efficient(n - 1) + fib_efficient(n - 2)
#         known[n] = ans
#         return ans


# numFibCalls = 0
# fibArg = 10

# print(fib(fibArg))
# print('function calls', numFibCalls)

# numFibCalls = 0


# print(fib_efficient(fibArg))
# print('function calls', numFibCalls)

def make_word_list():
    """Reads lines from a file and builds a list using append.

    returns: list of strings
    """
    word_list = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list

from bisect import bisect_left
def in_bisect(word_list, word):
    """Checks whether a word is in a list using bisection search.

    Precondition: the words in the list are sorted

    word_list: list of strings
    word: string
    """
    
    i = bisect_left(word_list, word)
    if i != len(word_list) and word_list[i] == word:
        return True
    else:
        return False


if __name__ == '__main__':
    word_list = make_word_list()

    for word in ['aa', 'alien', 'allen', 'zymurgy']:
        print(word, 'in list', in_bisect(word_list, word))



def has_duplicates(t):
    sort = t[:]
    sort.sort()
    for i in range(len(sort)-1):
        if sort[i] == sort[i+1]:
            return True