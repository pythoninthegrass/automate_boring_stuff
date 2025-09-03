#!/usr/bin/env python

# import random

# call module followed by its function
# random.randint(1, 10)

# from random import *

# call function w/o module
# non-standard usage and less preferred than module + function
# randint(1, 10)

# import sys
# print('Hello ')
# sys.exit
# print('Goodbye ')   # never runs ^^

# NON-STD LIBRARY
# pip install pyperclip
import pyperclip
pyperclip.copy('Hello world! ')
pyperclip.paste()
