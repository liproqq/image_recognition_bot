# bot for https://www.agame.com/game/magic-piano-tiles
# run on python 3.7

from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# X:  320 Y:  350 RGB: (186, 191, 235)
# X:  370 Y:  350 RGB: (  0,   0,   0)
# X:  450 Y:  350 RGB: (174, 178, 234)
# X:  530 Y:  350 RGB: (166, 171, 233)

tilesX = (320, 370, 450, 530)
tilesY = 450

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    for tile in tilesX:
        if pyautogui.pixel(tile,tilesY)[0] == 0:
            click(tile,tilesY)
