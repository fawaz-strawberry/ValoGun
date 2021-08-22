'''
923, 1074
right click
1017, 1217
left click
enter key
wait a sec
1617, 154
left click
repeat
'''

import time

import pyautogui

while True:
    #print(pyautogui.position())
    pyautogui.moveTo(400, 750)
    pyautogui.rightClick()

    pyautogui.moveTo(437, 800)
    pyautogui.leftClick()
    time.sleep(2)
    pyautogui.keyDown("enter")
    time.sleep(2)

    pyautogui.moveTo(1155, 61)
    pyautogui.leftClick()
    pyautogui.moveTo(814, 732)
    pyautogui.leftClick()
    time.sleep(1)
