#!/usr/bin/env python

# spam = 0
# while spam < 5:
#     print('Hello world ')
#     spam = spam + 1

spam = 0
while spam < 5:
    # spam = spam + 1
    spam += 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))
