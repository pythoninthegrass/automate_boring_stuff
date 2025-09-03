#!/usr/bin/env python

# lower/upper case
spam = 'Hello world!'
print(spam.lower())
print(spam.upper())

# Sanitize input
answer = input()
if answer.lower() == 'yes':
    print('Playing again')

# Test case
# print(spam.islower())                     # false
# print(spam.isupper())                     # false
print(f"""
islower is {spam.islower()}
isupper is {spam.isupper()}
Both methods are False because there's mixed cases
""")
print('Hello'.upper().isupper())            # true

# Other string test methods                 # all false lol
print(spam.isalpha())                       # letters only
print(spam.isalnum())                       # letters and numbers only
print(spam.isdecimal())                     # numbers only
print(spam.isspace())                       # whitespace only
print(spam.istitle())                       # titlecase only

print(spam[5].isspace())                    # TRUE!!!
print('hello world!'.title())               # remove `is` from methods to convert strings

# Start/endswith (not fuzzy matches, absolute)
print('Hello world!'.startswith('H'))       # true
print('Hello world!'.startswith('Hello'))   # true
print('Hello world!'.startswith('ello'))    # false
print('Hello world!'.endswith('world!'))    # true

# Join strings
print(','.join(['cats', 'rats', 'bats']))
print(''.join(['cats', 'rats', 'bats']))
print(' '.join(['cats', 'rats', 'bats']))
print(', '.join(['cats', 'rats', 'bats']))
print('\n\n'.join(['cats', 'rats', 'bats']))

# Split strings
print('My name is Simon'.split('m'))        # splits on whitespace by default

# Justify strings
print('Hello'.rjust(10))                    # right justify 10 characters
print('Hello'.ljust(10))                    # left justify 10 chars
print('Hello'.ljust(20, '*'))               # left justify 20 chars filled in with asterisks

# Center strings
print('Hello'.center(10, '='))              # center with approx amounts of chars filled in (control for char)

# Strip
# strip()                                     # strip whitespace on both sides
# lstrip()                                    # left strip
# rstrip()                                    # right strip
print('SpamSpamBaconSpamEggsSpamSpam'.strip('ampS'))    # remove capital 'S' and lower case 'a', 'm', and 'p'

# Replace
spam = 'Hello there!'
spam.replace('e', 'XYZ')

# pyperclip module
# import pyperclip
# pyperclip.copy('Hello!!!')
# pyperclip.paste()

# string interpolation w/conversion specifiers
name = 'Alice'
place = 'Main St'
time = '6pm'
food = 'Cadbury mini eggs'
'Hello %s, you\'re invited to a party at %s at %s. Please bring %s.' % (name, place, time, food)
