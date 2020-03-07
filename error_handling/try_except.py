#!/usr/bin/env python3

# def div_42_by(divide_by):
#     try:
#         return 42 / divide_by
#     except ZeroDivisionError:
#         print('Error: you tried to divide by zero ')

# print(div_42_by(2))
# print(div_42_by(12))
# print(div_42_by(0))
# print(div_42_by(1))

print('How many cats do you have? ')
num_cats = input()
try:
    if int(num_cats) >= 4:
        print('That is a lot of cats ')
    elif int(num_cats) >= 2:
        print("That's not that many cats ")
    elif int(num_cats) < 0:
        # technically also a ValueError that could be raised a la:
        # raise ValueError
        print("Strange choice of negative numbers, you got there ")
    else:
        print('Zero cats is also not that many cats ')
except ValueError:
    print("You didn't enter a number ")
