#!/usr/bin/env python

import random
import sys

print("Hello. What's your name? ")
name = input()

secret_number = random.randint(1, 20)
print("Well, " + name + ", I'm thinking of a number between 1 and 20. ")

# print("[DEBUG] Secret number is " + str(secret_number))

# Ask player to guess 6 times
for guesses_taken in range(1, 7):
    try:
        print("Take a guess. ")
        guess = int(input())
        if guess < 0:
            print('Strange choice of negative numbers, you got there ')
            raise ValueError
        elif guess < secret_number:
            print("Your guess is too low ")
        elif guess > secret_number:
            print("Your guess is too high ")
        else:
            break  # correct
    except ValueError:
        print(
            "Simple game accepts simple numbers. Please type a number (e.g., 50) "
        )
        continue
    except KeyboardInterrupt:
        print('\nKeyboard exception received. Exiting ')
        sys.exit(0)

if guess == secret_number:
    print("Good job, " + name + "! You guessed my number in " +
          str(guesses_taken) + " guesses! ")
else:
    print("Nope. The number I was thinking of was " + str(secret_number))
