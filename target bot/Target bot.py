import pyautogui 
import time
import keyboard
import random
import win32api, win32con

# Game: https://mouseaccuracy.com

time.sleep(2)

def click (x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
#color of center(239, 68, 68)

while keyboard.is_pressed('q') == False:

    pic = pyautogui.screenshot(region=(46,181,1849,836))

    width, height = pic.size

    for x in range (0,width,15):
        for y in range(0,height,15):
            
            r,g,b = pic.getpixel((x,y))

            if r == 239:
                click (x+46, y+181)
                time.sleep(0.01)
                break