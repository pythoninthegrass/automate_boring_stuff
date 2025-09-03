#!/usr/bin/env python

# SOURCES
# https://www.udemy.com/course/automate/learn/lecture/3470612#overview
# https://stackoverflow.com/questions/15340582/python-extract-pattern-matches

import bs4
import re
import requests

# Download URL
res = requests.get('https://automatetheboringstuff.com/2e/chapter7/')
res.raise_for_status()                                                              # blank = 200

# Parse HTML
soup = bs4.BeautifulSoup(res.text, 'html.parser')                                   # ignore parser warning

# Feed CSS selector into list of elements
elems = soup.select('p.noindent:nth-child(3)')                                      # first paragraph

# Get first index within list w/only text
par = elems[0].text.strip()                                                         # strips whitespace
num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')                                   # match digits delimited by dashes
print(num_regex.findall(par))                                                       # ['415-555-1234'] (note match obj vs. str)

# Scrape Automate the Boring Stuff's price from No Starch Press
def get_nspress_price(product_url):
    res = requests.get(product_url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('div.form-type-radio:nth-child(1) > label:nth-child(1)')    # Book + eBook $39.95
    sanitized_elems = elems[0].text.strip()

    price_regex = re.compile(r'(\$\d\d\.\d\d?)')                                    # non-greedy to match once
    dollar_dollar = (price_regex.search(sanitized_elems).group(1))                  # search to capture string that matched

    return dollar_dollar

price = get_nspress_price('https://nostarch.com/automatestuff2')
print(f"The price is {price}")
