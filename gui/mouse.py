#!/usr/bin/env python3

import pyautogui

width, height = pyautogui.size()                    # screen resolution
print(width, height)                                # 1440 900
pyautogui.position()                                # x,y coordinates
pyautogui.displayMousePosition()                    # real-time mouse coordinates (572 Y:  809 RGB: (NaN, NaN, NaN))

pyautogui.moveTo(10, 10, duration=1.5)              # absolutely move to top-left in 1.5 seconds
pyautogui.moveRel(200, 0, duration=1.5)             # relatively move 200 pixels to the right in 1.5s
pyautogui.moveRel(0, -100, duration=1)              # move 100 pixels up

pyautogui.click()                                   # click current cursor location
pyautogui.click(339, 38)                            # click at x,y
pyautogui.doubleClick(339, 38)
