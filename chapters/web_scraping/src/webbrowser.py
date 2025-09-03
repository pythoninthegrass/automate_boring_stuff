#!/usr/bin/env python

import webbrowser
import sys
import pyperclip

# TODO: argparse instead of `sys.argv`
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

def main():
    webbrowser.open('http://google.com/maps/place/' + address)

if __name__ == '__main__':
    main()
