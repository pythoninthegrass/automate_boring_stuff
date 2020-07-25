#!/usr/bin/env python3

import pyautogui

pyautogui.click(100, 100); pyautogui.typewrite('Hello world!\n', interval=0.2)
pyautogui.click(100, 100); pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'], interval=1)

# TODO: test Mac hotkeys
pyautogui.press('f1')
pyautogui.hotkey('ctrl', 'o')
