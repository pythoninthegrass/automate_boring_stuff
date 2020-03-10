#!/usr/bin/env python3

# spam = ['hello', 'hi', 'howdy', 'heyas']
# # list.method('string')
# print(spam.index('hello'))

# edit list in-place (mutable)
# spam = ['cat', 'dog', 'bat']
# spam.append('moose')
# spam.insert(1, 'chicken')
# .remove: removes first instance anywhere in list; not tied to index like del
# e.g., del spam[0]
# spam.remove('cat') 
# print(spam)

# spam = [2, 5, 3.14, 1, -7]
spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants'] # ASCII-betical order (uppercase first)
spam.sort(key=str.lower) # true alphabetical order (e.g., A, a, Z, z)
spam.sort(reverse=True) # can't mix int and strings when calling sort method
print(spam)