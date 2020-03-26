#!/usr/bin/env python3

import re

def phone_number(text):
    if len(text) != 12:
        return False                                        # not phone number length
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False                                    # no area code
    if text[3] != '-':
        return False                                        # missing dash
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False                                    # missing first three chars
    if text[7] != '-':
        return False                                        # missing dash
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False                                    # missing last four chars
    return True                                             # if str passes above criteria, it matches

# print(phone_number('415-555-1234'))

call_me = '415-555-1011'
maybe = '415-555-9999'
msg = f'Call me maybe at {call_me} and/or {maybe}.'         # f-strings
# msg = 'Call me maybe at %s and/or %s.' % (call_me, maybe) # conversion specifiers
found_number = False
for i in range(len(msg)):
    chunk = msg[i:i+12]                                     # slice strings up to 12 chars
    if phone_number(chunk):
        print(f'Phone number found: {chunk}.')
        found_number = True
if not found_number:
    print('The cake is a lie.')

num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')           # raw string (avoid escapes) - match digits delimited by dashes
# mo = num_regex.search(msg)                                # returns first match object searching message via regex
# print(mo.group())                                         # search method followed by group method
print(num_regex.findall(msg))                               # returns first match object searching message via regex
