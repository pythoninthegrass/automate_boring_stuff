#!/usr/bin/env python

spam = ['hello', 'hi', 'howdy', 'heyas']
# list.method('string')
print(spam.index('hello'))

# edit list in-place (mutable)
spam = ['cat', 'dog', 'bat']
spam.append('moose')
spam.insert(1, 'chicken')
# # .remove: removes first instance anywhere in list; not tied to index like del
# # e.g., del spam[0]
spam.remove('cat')
print(spam)

# spam = [2, 5, 3.14, 1, -7]
spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants'] # ASCII-betical order (uppercase first)
spam.sort(key=str.lower) # true alphabetical order (e.g., A, a, Z, z)
spam.sort(reverse=True) # can't mix int and strings when calling sort method
print(spam)

# lists vs. strings
spam = [0, 1, 2, 3, 4, 5]
cheese = spam # assign referenced list
cheese[1] = 'Hello!'
print(cheese)   # identical output
print(spam)     # to this

# changes made to list in function affect list outside of function
def eggs(cheese):
    cheese.append('Goodbye') # call append method

spam = [1, 2, 3]    # uses same referenced list from function
eggs(spam)
print(spam)

import copy

spam = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(spam)    # uses completely new list -- not referenced list
cheese[1] = 42
print(cheese)
print(spam)

# line continuation
spam = ['apples',
        'oranges,'
        'bananas',
        'cats']
print('Four score and seven ' + \
    'years ago')
