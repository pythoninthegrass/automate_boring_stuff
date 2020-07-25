#!/usr/bin/env python3

import os
import pyautogui

# `cd` to directory for screenshots
cwd = os.getcwd() + '/resources'
os.chdir(cwd)
home = os.getenv("HOME")

# TODO: timestamp date/time
pyautogui.screenshot(f"{cwd}/screenshot.png")
pyautogui.locateOnScreen(f"{home}/Downloads/Screen Shot 2020-06-29 at 8.35.55 PM.png")
pyautogui.locateCenterOnScreen(f"{home}/Downloads/Screen Shot 2020-06-29 at 8.35.55 PM.png")
pyautogui.moveTo((932, 336), duration=1)    # move cursor