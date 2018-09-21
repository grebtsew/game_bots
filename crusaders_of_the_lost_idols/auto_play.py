import keyboard
import pyautogui
import random
from threading import Thread
import time
import msvcrt
import datetime
'''
This program auto plays crusader of the lost idols
A game thats free to play on steam!
This program will:
* go to next level
* close ads
* update and complete missions
* use functions
* upgrade characters

Usage:
1. Start the game (in left corner)
2. Run this program
3. Put main focus on game

Game window size: 1260, 900
'''
class WINDOW_SIZE_STRUCT():
    x = 0
    y = 0

WINDOW_SIZE = WINDOW_SIZE_STRUCT()
WINDOW_SIZE.x = 1260
WINDOW_SIZE.y = 900

bot_running = True

def wait(t, range = 0):
    time.sleep(t + random.uniform(0, range))

def next_level(delay):
    print(str(datetime.datetime.now()) + " next level " + str(delay))
    pyautogui.press('right')
    wait(30+delay, 3+delay)

def upgrade_all( delay):
    print(str(datetime.datetime.now()) +" upgrade")
    pyautogui.click(927/1260 ,638/900 )
    wait(1,0)
    pyautogui.click(1235/1260 , 691)
    wait(1,1)
    pyautogui.click(500, 500)
    wait(1,1)
    pyautogui.click(1235, 839)
    wait(1,1)
    pyautogui.click(500, 500)
    pyautogui.moveTo(680, 450, duration=0.25)
    wait(40 + delay, 3+ delay)

def activate_functions(delay):
    wait(1,1)
    print(str(datetime.datetime.now()) +" activate functions")
    pyautogui.click(450, 624)
    wait(1,1)
    pyautogui.click(510, 625)
    wait(1,1)
    pyautogui.click(560, 625)
    wait(1,1)
    pyautogui.click(610, 625)
    wait(1,1)
    pyautogui.click(660, 625)
    wait(1,1)
    pyautogui.click(710, 625)
    wait(1,1)
    pyautogui.click(760, 625)
    wait(1,1)
    pyautogui.click(810, 625)
    pyautogui.moveTo(680, 450, duration=0.25)
    wait(300+delay, 30+delay)

def remove_add(delay):
    print(str(datetime.datetime.now()) +" remove add")
    wait(1,1)
    pyautogui.click(949,113)
    wait(1000+delay,10+delay)

def missions(delay):
    wait(1,1)
    print(str(datetime.datetime.now()) +" fix missions")
    pyautogui.click(1069, 636) # tab
    wait(1,1)

    pyautogui.click(179, 763) # open
    wait(1,1)

    #fix auto pop
    for k in range(10):
        pyautogui.click(694,500) # open
        wait(3,1)
        pyautogui.click(694,519) # open
        wait(2,1)

    for i in range(10):
        pyautogui.click(185,165) #mission
        wait(1,1)
        for j in range(10):
            pyautogui.click(125,736) #character
            wait(1,1)
        pyautogui.click(1082,592) # start
        wait(1,1)
        pyautogui.click(538,532) # accept
        wait(1,1)
        pyautogui.click(694,519) # open

    pyautogui.click(1182, 85) # close
    wait(1,1)
    pyautogui.moveTo(680, 450, duration=0.25)

    wait(600+delay, 30+delay)

def hook():
    while bot_running:

        # Press key always if "ctrl+k" is pressed
        if(keyboard.is_pressed('ctrl+k')):
            wait(1)
            while not keyboard.is_pressed('ctrl+k'):
                wait(0.1, 0.1)
                pyautogui.click()

        if(keyboard.is_pressed('esc')):
            bot_running = False


def perform(func):
    counter = 0
    while bot_running:
        func(counter)
        counter += 1

def main():
    thread = Thread(target=hook)
    thread.start()

    wait(1,1) # random upstart

    #press next level every
    thread = Thread(target= perform, args=(next_level,))
    thread.start()

    wait(1,1) # random upstart
    exit(0)
    #upgrade max levels
    thread = Thread(target= perform, args=(upgrade_all,))
    thread.start()
    wait(1,1) # random upstart

    #add
    thread = Thread(target= perform, args=(remove_add,))
    thread.start()

    #functions
    thread = Thread(target= perform, args=(activate_functions,))
    thread.start()

    wait(100,1) # random upstart

    #missions
    thread = Thread(target= perform, args=(missions,))
    thread.start()

if __name__ == "__main__":
    main()
