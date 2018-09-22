import keyboard
import pyautogui
import random
from threading import Thread
import time
import msvcrt
import datetime

'''
This file contains core functions used in bots for specific games
'''

bot_running = True


def hook(k_func = None, delay = 1):
    global bot_running
    while bot_running:

        # Press key always if "ctrl+k" is pressed
        if(keyboard.is_pressed('ctrl+k')):

            if k_func is not None:
                k_func()

        if(keyboard.is_pressed('esc')):
            print(str(datetime.datetime.now()) +" close program, will wait for waiting threads before closing!")
            bot_running = False
            exit(delay)


def perform(func):
    global bot_running

    counter = 0
    while bot_running:
        func(counter)
        counter += 1


class WINDOW_SIZE_STRUCT():
    x = 0
    y = 0

def wait(t, range = 0):
    time.sleep(t + random.uniform(0, range))
