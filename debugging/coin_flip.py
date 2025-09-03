#!/usr/bin/env python

import random

heads = 0

for i in range(1, 1001):
    if random.randint(0, 1) == 1:
        heads += 1
    if i == 500:
        print('Halfway done! ')                     # breakpoints

print('Heads came up ' + str(heads) + ' times. ')
