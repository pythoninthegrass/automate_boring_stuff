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

# reserved characters in regex (escape to match)
# .  ^  $  *  +  ?  {  }  [  ]  \  |  (  )
regex = re.compile(r'\+\*\?')
regex.search('I learned about +*? regex syntax')

# digit matching
num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')           # raw string (avoid escapes) - match digits delimited by dashes
# mo = num_regex.search(msg)                                # returns first match object searching message via regex
# print(mo.group())                                         # search method followed by group method
print(num_regex.findall(msg))                               # returns first match object searching message via regex

# groups
num_regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = num_regex.search(msg)
mo.group(1)

# escape parentheses
num_regex = re.compile(r'\(\d\d\d\) (\d\d\d)-(\d\d\d\d)')
mo = num_regex.search('My number is (415) 555-4242')
mo.group(0)

# multiple queries
bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = bat_regex.search('Batmobile lost a wheel')
mo.group()                                                  # error handling: IndexError and NoneType

# match zero or one times via `?`
bat_regex = re.compile(r'Bat(wo)?man')
mo = bat_regex.search('The Adventures of Batman')
mo.group()

num_regex = re.compile(r'(\d\d\d)?-\d\d\d-\d\d\d\d')
mo = num_regex.search(msg)
mo.group()

# match zero or more times via `*`
bat_regex = re.compile(r'Bat(wo)*man')
mo = bat_regex.search(r'The Adventures of Batwowowowoman')
mo.group()

# match one or more times via `+` (once is mandatory for match)
bat_regex = re.compile(r'Bat(wo)+man')
mo = bat_regex.search('The Adventures of Batman')           # NoneType
mo.group()

# exact match w/shorthand `{3}`
# ha_regex = re.compile(r'(Ha)(Ha)(Ha)')
ha_regex = re.compile(r'(Ha){3}')
ha_regex.search("He said 'HaHaHa'")

# exact match after: 
# optional `?` area code
# phone number sans area code
# optional `,` `?` comma delimiter (list)
# optional `.` `?` whitespace/chars
# or one or more `.` `+` whitespace/chars
# occurring exactly 3 times `{3}` 
num_regex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?(.)?|(.)+){3}')
num_regex.search("My numbers are 415-555-1234, 555-4242, and 212-555-0000")

# match minimum/maximum
# ha_regex = re.compile(r'(Ha){3,}')                        # 3 min, unbounded max
# ha_regex = re.compile(r'(Ha){,5}')                        # unbounded min, 5 max
ha_regex = re.compile(r'(Ha){3,5}')
ha_regex.search("He said 'HaHaHaHaHa'")                      # matches between 3 - 5 instances; caps at 5 Ha's

dig_regex = re.compile(r'(\d){3,5}')                        # greedy match: longest string possible        # 12345
dig_regex = re.compile(r'(\d){3,5}?')                       # non-greedy match: smallest string possible   # 123
dig_regex.search("1234567890")
