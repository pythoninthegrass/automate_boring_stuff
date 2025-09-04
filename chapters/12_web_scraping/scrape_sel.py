#!/usr/bin/env python

# import logging
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('http://popurls.com')

# TODO: try/except for refreshed css selectors
def main():
    # The Verge - 'Apple granted patent for software that would let you take socially distant group selfies'
    elem = browser.find_element_by_css_selector('#gr_theverge > div:nth-child(1) > h4:nth-child(1) > a:nth-child(2)')
    elem.click()

    # Get open tabs/windows
    windows = browser.window_handles
    browser.switch_to.window(windows[0])                                        # 0: first tab/window

    # List of paragraphs
    elems = browser.find_element_by_css_selector('p')

    # Search input
    search_elem = browser.find_element_by_css_selector('#q')

    # Search for 'Just 29 Finger Tattoos That Look Cool'
    # http://popurls.com/go/pop/lcd7b31f744b94b11a7b06fa5a9a2f182
    search_elem.send_keys('finger tattoos')
    search_elem.submit()
    time.sleep(5)
    browser.close()

    # Navigation
    # browser.back()
    # browser.forward()
    # browser.refresh()
    # browser.close()                                                           # close tab/window (quits if last tab)
    # browser.quit()

    # Read content
    elem = browser.find_element_by_css_selector(
        '#gr_theverge > div:nth-child(1) > h4:nth-child(1) > a:nth-child(2)'
        )
    elem.text                                                                   # Alt text: 'Apple granted patent for software...'
    elem = browser.find_element_by_css_selector('html')                         # Entire webpage (inspect source)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as k:
        # logging.info(f"{k} exception occurred ", exc_info=True)
        print('\nKeyboard exception received. Exiting ')
        browser.quit()
        sys.exit(0)
    except Exception:
        # logging.error("Uncaught exception occurred. Exiting ", exc_info=True)
        print("\nUncaught exception occurred. Exiting ")
        browser.quit()
        sys.exit(1)
