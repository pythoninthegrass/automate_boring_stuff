#!/usr/bin/env python

import os
import traceback

# raise generic exception
raise Exception('This is the error message. ')

# raise specific exception based on function calls
# expected user/program errors (e.g., file not found, invalid input)
"""
***************
*             *
*             *
*             *
***************

"""
def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("'symbol' needs to be a string with one character length")
    if (width < 2) or (height < 2):
        raise Exception("'width' and 'height' must be greater or equal to two character length")
    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)

box_print('*', 15, 5)                                       # box in docstrings ^^
box_print('O', 5, 16)                                       # super skinny tall box of O's
box_print('**', 15, 5)                                      # broken mirror box due to two chars (raise exception)
box_print('*', 1, 1)                                        # 1x1 box isn't a box (raise exception)

# traceback formatting
print(os.getcwd())

try:
    raise Exception('This is the error message.')
except:
    error_file = open('./debugging/error.log', 'a')
    error_file.write(traceback.format_exc())
    error_file.close()
    print('The traceback info was written to error.log')

# assertions (sanity check) - crashes program as it's conditions are always true
# programming errors that aren't meant to be recovered from
assert False, 'This is the error message'

# dictionary w/cardinal directions
market_2nd = {'ns': 'green', 'ew': 'red'}

def switch_lights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)

switch_lights(market_2nd)
