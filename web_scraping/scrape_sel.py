#!/usr/bin/env python3

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://popurls.com)

# The Verge - 'Apple granted patent for software that would let you take socially distant group selfies'
elem = browser.find_element_by_css_selector('#gr_theverge > div:nth-child(1) > h4:nth-child(1) > a:nth-child(2)')
elem.click()

# List of paragraphs
elems = browser.find_element_by_css_selector('p')

# Search input
search_elem = browser.find_element_by_css_selector('#q')

# Search for 'Just 29 Finger Tattoos That Look Cool'
# http://popurls.com/go/pop/lcd7b31f744b94b11a7b06fa5a9a2f182
search_elem.send_keys('finger tattoos')
search_elem.submit()

# Navigation
browser.back()
browser.forward()
browser.refresh()
browser.quit()

# Read content
elem = browser.find_element_by_css_selector(
    '#gr_theverge > div:nth-child(1) > h4:nth-child(1) > a:nth-child(2)'
    )
elem.text                                                                   # Article alt text
elem = browser.find_element_by_css_selector('html')                         # Entire webpage (inspect source)
