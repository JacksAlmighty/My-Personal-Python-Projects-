import pyautogui
import time
import keyboard
import win32api, win32con
import random 
import os


while 1: 
    try:
        if pyautogui.locateOnScreen(r"C:\Users\Jackson\Desktop\target bot\target.png", region = (46,181,1849,836) grayscale=True, confidence = .8) != None:
            print("I can see it!")
            time.sleep(0.5)
        else:
            print("I cant see it")
            time.sleep(0.5)
    except pyautogui.ImageNotFoundException:
        print("I cant see it")
        time.sleep(0.5)