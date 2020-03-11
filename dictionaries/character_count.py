#!/usr/bin/env python3

import pprint

message = 'It was a bright cold day in April and the clocks were striking thirteen.'
count = {}

# for character in message:
for character in message.upper():
    count.setdefault(character, 0)
    count[character] += 1

# ugly, random output
# print(count)

# single column key-value pairs
# pprint.pprint(count)

# string of key-value pairs
print(pprint.pformat(count))