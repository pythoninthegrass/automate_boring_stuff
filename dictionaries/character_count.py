#!/usr/bin/env python

import pprint

# message = 'It was a bright cold day in April and the clocks were striking thirteen.'
# multiline string escapes characters automatically while retaining formatting
message = '''
Your bones don't break, mine do. That's clear.
Your cells react to bacteria and viruses differently than mine. You don't get sick, I do. That's also clear.
But for some reason, you and I react the exact same way to water.
We swallow it too fast, we choke.
We get some in our lungs, we drown.
However unreal it may seem, we are connected, you and I.
We're on the same curve, just on opposite ends.
'''

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
