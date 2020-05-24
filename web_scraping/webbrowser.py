#!/usr/bin/env python3

# TODO: `setuptools`
import webbrowser
import sys
import pyperclip

# TODO: argparse instead of `sys.argv`
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('http://google.com/maps/place/' + address)