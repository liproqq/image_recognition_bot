# bot for aimbooster.com

from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# time to switch to the screen
time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

color = (255, 219, 195)

while keyboard.is_pressed('q') == False:

    pic = pyautogui.screenshot(region=(660,350,600,400))

    width, height = pic.size

    # check every fifth pixel for bulls eye
    for x in range(0,width,5):
        for y in range(0,height,5):

            # r,g,b = pic.getpixel((x,y))

            if pic.getpixel((x,y)) == color:
                click(x+660,y+350)
                #prevent premature clicks
                time.sleep(0.05)
                break