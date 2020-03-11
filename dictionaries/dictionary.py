#!/usr/bin/env python3

# dictionaries are unordered, unlike lists
my_cat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
# print(my_cat['size'])
print('My cat has ' + my_cat['color'] + ' fur.')

eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
print('name' in eggs)       # in/not in
print(list(eggs.keys()))    # keys only
print(list(eggs.values()))  # values only
print(list(eggs.items()))   # key-value pairs (tuples)

# for k in eggs.keys():
#     print(k)

# for k, v in eggs.items():
#     print(k, v)

# tedious
# if 'color' in eggs:
#     print(eggs['color'])

# get method
# check if value exists, if not, return 0
# avoids KeyError traceback
print(eggs.get('age', 0))

picnic_items = {'apples': 5, 'cups': 2}
print("I'm bringing " + str(picnic_items.get('napkins', 0)) + ' to the picnic. ')

# setdefault method
# adds new key-value pair
print(eggs.setdefault('color', 'black'))    # black
print(eggs.setdefault('color', 'orange'))   # black (FAIL)