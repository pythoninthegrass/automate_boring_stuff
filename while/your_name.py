#!/usr/bin/env python3

name = ''
while name != 'your name':
    print("Please type 'your name'. ")
    name = input()
print('Thank you! ')

# BROKEN ON PYTHON3.7
# name = ''
# while True:
#     print("Please type 'your name'. ")
#     if name == 'your name':
#         break
# print('Thank you! ')