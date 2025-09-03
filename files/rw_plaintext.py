#!/usr/bin/env python

import os
import shelve

# read file
os.getcwd()                                         # `pwd`
hello_file = open('./resources/hello.txt')          # read-only by default 'r'
content = hello_file.read()                         # 'Hello world!\nHow are you?'          # single string
print(content)                                      # ^^ w/newlines pretty printed
hello_file.readlines()                              # ['Hello world!\n', 'How are you?']    # list of str
hello_file.close()                                  # quit file

# write file
hello_file = open('./resources/hello2.txt', 'w')    # creates file if it doesn't exist
hello_file.write('Hello!!!!!')                      # returns bytes written; no newline is created by default
hello_file.close()
bacon_file = open('./resources/bacon.txt', 'w')
bacon_file.write('Bacon is not a vegetable.')
bacon_file.close()

# append file
bacon_file = open('./resources/bacon.txt', 'a')
bacon_file.write('\n\nBacon is delicious.')
bacon_file.close()

# shelve module
shelf_file = shelve.open('./resources/my_data')     # store values in bin; returns dictionary-like value
shelf_file['cats'] = ['Zophie', 'Pooka', 'Simon',
                    'Fat-tail', 'Cleo']
shelf_file.close()

shelf_file = shelve.open('./resources/my_data')
shelf_file['cats']                                  # ['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']
shelf_file.close()

shelf_file = shelve.open('./resources/my_data')
shelf_file.keys()
list(shelf_file.keys())                             # ['cats']
list(shelf_file.values())                           # [['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']]
shelf_file.close()
