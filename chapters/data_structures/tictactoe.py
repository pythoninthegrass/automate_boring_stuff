#!/usr/bin/env python

import pprint

# tic-tac-toe board (dictionary)
the_board = {
    'top-L': ' ',
    'top-M': ' ',
    'top-R': ' ',
    'mid-L': ' ',
    'mid-M': ' ',
    'mid-R': ' ',
    'low-L': ' ',
    'low-M': ' ',
    'low-R': ' '
}
# pprint.pprint(the_board)

the_board['low-R'] = 'X'
the_board['mid-M'] = 'X'
the_board['mid-L'] = 'X'
the_board['top-L'] = 'O'
the_board['top-M'] = 'O'
the_board['top-R'] = 'O'
# pprint.pprint(the_board)

def print_board(board):
    print(board['top-L'] + '|' + board['top-M']+ '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M']+ '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M']+ '|' + board['low-R'])

print_board(the_board)

# check data type
print(type(42))
print(type('hello'))
print(type(3.14))
print(type(the_board['top-R']))
