

import math
def nested_sum(t):
    """Computes the total of all numbers in a list of lists.

    t: list of list of numbers

    returns: number

    Expected output:
    # >>> t = [[1, 2], [3], [4, 5, 6]]
    # >>> nested_sum(t)
    21
    """
    # total = 0
    # for nested in t:
    #     total += sum(nested)
    # return total
# print(nested_sum)

# t = [1, 2, 3]
def cumsum(t):
    """Computes the cumulative sum of the numbers in t.

    t: list of numbers

    returns: list of numbers

    Expected output:
    >>> t = [1, 2, 3]
    >>> cumsum(t)
    [1, 3, 6]
    # """
    # t = [1, 2, 3]
    # total = 0
    # res = []
    # for x in t:
    #     total += x
    #     res.append(total)
    #     print('current list:')
    #     print (res)
    # return res





#"""Returns all but the first and last elements of t.
#   t: list

 #   returns: new list

  #  Expected output:
   # >>> t = [1, 2, 3, 4]
    #>>> middle(t)
   # [2, 3]
    
# t= [1,2,3,4]
# t= t[1:-1]
# print(t)

# def middle (t):
#     return t[1:-1]

# t= [1,2,3,4,5,6,7]
# print (middle(t))
# print (t)



t = [1, 2, 3, 4]
def chop(t):
    t. remove (t[1])
    return t

t= [1,2,3,4]
print (chop(t))


def is_sorted(t):
    """Checks whether a list is sorted.

    t: list

    returns: boolean

    Expected output:
    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted(['b', 'a'])
    False
    """
#     return t == sorted(t)

# print (is_sorted([1,2,2]))
# # print (is_sorted(['b','a']))

# def is_sorted(t):
#     previous= t[0]
#     for c in t:
#         if c< previous:
#             return False
#         previous=c
#     return True

# print(is_sorted(['a','b','c','d']))
# print(is_sorted(['a','b','c','a']))


def is_anagram(word1, word2):
    """Checks whether two words are anagrams

    Two words are anagrams if you can rearrange the letters from one to 
    spell the other.

    word1: string or list
    word2: string or list

    returns: boolean

    Expected output:
    >>> is_anagram('stop', 'pots')
    True
    >>> is_anagram('different', 'letters')
    False
    >>> is_anagram([1, 2, 2], [2, 1, 2])
    Ture
    """
#     return sorted(word1) == sorted(word2)
# print(is_anagram('stop', 'pots'))
# print (is_anagram('different', 'letters'))
# print (is_anagram([1, 2, 2], [2, 1, 2]))

def has_duplicates(s):
    """Returns True if any element appears more than once in a sequence.

    s: string or list

    returns: bool

    output:
    >>> print(has_duplicates('cba'))
    False
    >>> print(has_duplicates('abba'))
    True
    """
    t = list(s)
    t.sort()

#   
#     for i in range(len(t)-1):
#         if t[i] == t[i+1]:
#             return True
#     return False
# print(has_duplicates('cba'))
# print(has_duplicates('abba'))


def has_adjacent_duplicates(s):
    """Returns True if there are two same adjacent elements.

    s: string or list

    returns: bool

    output:
    >>> print(has_adjacent_duplicates('cba'))
    False
    >>> print(has_adjacent_duplicates('abca'))
    Flase
    >>> print(has_adjacent_duplicates('abbc'))
    True
    """
#     t = list(s)
#     t.sort()
#     for i in range(len(t)-1):
#         if t[i] == t[i+1]:
#             return True
#     return False

# print(has_adjacent_duplicates('cba'))
# print(has_adjacent_duplicates('abca'))
# print(has_adjacent_duplicates('abbc'))

# def main():
#     t = [[1, 2], [3], [4, 5, 6]]
#     print(nested_sum(t))

#     t = [1, 2, 3]
#     print(cumsum(t))

#     t = [1, 2, 3, 4]
#     print(middle(t))
#     chop(t)
#     print(t)

#     print(is_sorted([1, 2, 2]))
#     print(is_sorted(['b', 'a']))

#     print(is_anagram('stop', 'pots'))
#     print(is_anagram('different', 'letters'))
#     print(is_anagram([1, 2, 2], [2, 1, 2]))

#     print(has_duplicates('cba'))
#     print(has_duplicates('abba'))


# if __name__ == '__main__':
#     main()
