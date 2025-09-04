#!/usr/bin/env python

# SOURCE
# http://echrislynch.com/2018/07/13/turning-a-pdf-into-a-pandas-dataframe/

import pandas as pd
import PyPDF2

# import pyperclip
import re

# create a regex for phone numbers
phone_regex = re.compile(r'''
    # 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
    (
    ((\d\d\d)|(\(\d\d\d)))?                                                 # area code (optional)
    (\s|-)                                                                  # first separator
    \d\d\d                                                                  # first 3 digits
    -                                                                       # separator
    \d\d\d\d                                                                # last 4 digits
    ((ext(\.)?\s)|x)                                                        # extension word-part (optional)
    (\d{2,5}))?                                                             # extension number-part (optional)
    )
''', re.VERBOSE)
# one-liner ^^
# re.compile('((\d\d\d)|(\(\d\d\d)))?(\s|-)\d\d\d-\d\d\d\d((ext(\.)?\s)|x)(\d{2,5}))?')

# create a regex for emails
email_regex = re.compile(r'''
    #some.+_thing@something.com
    [a-zA-Z0-9_.+]+                                                         # name part
    @                                                                       # @ symbol
    [a-zA-Z0-9_.+]+                                                         # domain name part
''', re.VERBOSE)

# get the text off the clipboard
# text = pyperclip.paste()

# TODO: read from PDF w/pandas
pdf_file_obj = open('../files/phone_book.pdf')
pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)

# extract the email/phone from text
extracted_phone = phone_regex.findall(text)
extracted_email = email_regex.findall(text)

all_phone_nums = []
for num in extracted_phone:
    all_phone_nums.append(num[0])

print(all_phone_nums)

# copy extracted email/phone to the clipboard
results = '\n'.join(all_phone_nums) + '\n' + '\n'.join(extracted_email)     # one phone number per line
# pyperclip.copy(results)
