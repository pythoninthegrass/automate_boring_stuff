#!/usr/bin/env python3

# global scope
spam = 42           # global var

# local scope
def eggs():
    # global spam   # convert local to global var
    spam = 42       # local var

# global scope
print('Some code here. ')
print('Some more code. ')