#!/usr/bin/env python

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
ha_regex.search("He said 'HaHaHaHaHa'")                     # matches between 3 - 5 instances; caps at 5 Ha's

dig_regex = re.compile(r'(\d){3,5}')                        # greedy match: longest string possible        # 12345
dig_regex = re.compile(r'(\d){3,5}?')                       # non-greedy match: smallest string possible   # 123
dig_regex.search("1234567890")

# findall
num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')           # list of strings: zero or one groups
num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')       # tuples of strings: two or more groups
num_regex.findall('My numbers are 415-555-1234, 555-4242, '
                'and 212-555-0000'
                )

# character classes
# \d - digits
# \D - non-digits
# \w - any letter, digit, or underscore (word chars)
# \W - inverse ^^
# \s - space, tab, or newline (space chars)
# \S - inverse ^^
# + - one or more occurrences

lyrics = '''
12 drummers drumming, 11 pipers piping,
10 lords a leaping, 9 ladies dancing, 8 maids a milking,
7 swans a swimming, 6 geese a laying, 5 golden rings,
4 calling birds, 3 french hens, 2 turtle doves, 1 partridge
in a pear tree
'''
xmas_regex = re.compile(r'\d+\s\w+')
xmas_regex.findall(lyrics)

# custom character classes
vowel_regex = re.compile(r'[AEIOUaeiou]')                   # match all vowels
double_vowel_regex = re.compile(r'[AEIOUaeiou]{2}')         # match repeated vowels
consonants_regex = re.compile(r'[^AEIOUaeiou]')             # negative matching (inverse) (dragnet for punctuation and digits)
consonants_regex.findall('Robocop eats baby food.')

# starts with
begins_regex = re.compile(r'^Hello')
begins_regex.search('Hello there!')

# ends with
ends_regex = re.compile(r'world!$')
ends_regex.search('Hello world!')

# match all digits
all_regex = re.compile(r'^\d+$')
all_regex.search('123456789')

# wildcard - match anything but newline `\n`
at_regex = re.compile(r'[Aa]t.')                            # match 'At ' (with whitespace)
at_regex = re.compile(r'[Aa]t.{1,2}')                       # match 'At t'
at_regex.findall('At the Drive-In')

# dot-star - match any character zero or more times
'First Name: Al Last Name: Sweigart'.find(':') + 2          # get index of first name
'First Name: Al Last Name: Sweigart'[12:]                   # start arithmetic for last name string slicing
name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')# match any char `.` zero or more times `*` after 'First/Last Name:'
name_regex.findall(r'First Name: Al Last Name: Sweigart')   # '[Al Sweigart']

# dot-star non-greedy
serve = '<To serve humans> for dinner.>'
nongreedy = re.compile(r'<(.*?)>')                          # find anything within open/closed chevrons - stop after first match
nongreedy.findall(serve)                                    # ['To serve humans']

# dot-star greedy
serve = '<To serve humans> for dinner.>'
greedy = re.compile(r'<(.*)>')                              # find anything within open/closed chevrons - match all instances
greedy.findall(serve)                                       # ['To serve humans> for dinner.']

# robocop prime directive matching w/greedy dot-star
prime = 'Serve the public trust.\nProtect the innocent.\nUphold the law.'
dot_star = re.compile(r'.*')
dot_star.search(prime)                                      # < ... match='Serve the public trust.'>
dot_star = re.compile(r'.*', re.DOTALL)                     # force matching newline chars
dot_star.search(prime)                                      # < ... match='Serve the public trust.\nProtect the innocent.\nU>

# case insensitive
vowel_regex = re.compile(r'[aeiou]')                        # only match lowercase vowels
vowel_regex.findall('Al, why u like robocop so much?')      # ['u', 'i', 'e', 'o', 'o', 'o', 'o', 'u']
vowel_regex = re.compile(r'[aeiou]', re.IGNORECASE)         # match lowercase vowel, ignore case (i.e., [AEIOUaeiou])
vowel_regex.findall('Al, why u like robocop so much?')      # ['A', 'u', 'i', 'e', 'o', 'o', 'o', 'o', 'u']

# sub method
names_regex = re.compile(r'Agent \w+')                                          # one or more word chars
names_regex.findall('Agent Alice gave '                     # ['Agent Alice', 'Agent Bob']
                    'the secrets to Agent Bob'
                    )
names_regex.sub('REDACTED', 'Agent Alice gave '             # 'REDACTED gave the secrets to REDACTED'
                'the secrets to Agent Bob'
                )
names_regex = re.compile(r'Agent (\w)\w*')                  # one word character followed by zero or more letters
names_regex.findall('Agent Alice gave '                     # ['A', 'B']
                    'the secrets to Agent Bob'
                    )
names_regex.sub(r'Agent \1****', 'Agent Alice gave '        # 'Agent A**** gave the secrets to Agent B****'
                'the secrets to Agent Bob'
                )

# verbose mode
num_regex = re.compile(r'''
(\d\d\d)|                                                   # area code w/o parens, w/dash
(\(\d\d\d\))                                                # area code w/parens, w/o dash
-                                                           # first dash
\d\d\d                                                      # first 3 digits
-                                                           # second dash
\d\d\d\d                                                    # last 4 digits
\sx\d{2,4}                                                  # ext (e.g., x1234)
''', re.IGNORECASE | re.DOTALL | re.VERBOSE)                # bitwise OR operator: `|` to chain arguments (DOTALL == everything incl. newline)
num_regex.search("My numbers are 415-555-1234, 555-4242, and 212-555-0000 x1234")
