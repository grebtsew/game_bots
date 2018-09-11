import cv2 # old
import pyautogui
from random import randint
from threading import Thread
import time
import msvcrt

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


def wait(t, range):
    time.sleep(t + randint(0,range))

def next_level():
    while(True):
        # smallscreen mode
        # press (1177, 301)
        # wait 30 sec
        print("clicked next level")
        #pyautogui.click(1177, 301)
        pyautogui.press('right')
        wait(30, 3)

def upgrade_all():
    while(True):
        # smallscreen mode
        # upgrade all sometimes
        print("upgrade")
        pyautogui.click(927,638)
        wait(1,0)
        pyautogui.click(1235, 691)
        wait(1,1)
        pyautogui.click(500, 500)
        wait(1,1)
        pyautogui.click(1235, 839)
        wait(1,1)
        pyautogui.click(500, 500)
        pyautogui.moveTo(680, 450, duration=0.25)

        wait(40, 3)

def activate_functions():
    while(True):
        wait(1,1)
        print("activate functions")
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
        wait(300, 30)

def remove_add():
        while(True):
            wait(1,1)
            pyautogui.click(949,113)
            wait(1000,10)

def missions():
    while(True):
        wait(1,1)
        print("activate functions")
        pyautogui.click(1069, 636) # tab
        wait(1,1)

        pyautogui.click(179, 763) # open
        wait(1,1)

        #fix auto pop
        for k in range(10):
            pyautogui.click(694,519) # open
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

        wait(600, 30)


def main():
    wait(1,1) # random upstart

    #press next level every
    thread = Thread(target = next_level)
    thread.start()

    wait(1,1) # random upstart

    #upgrade max levels
    thread = Thread(target = upgrade_all)
    thread.start()

    wait(1,1) # random upstart

    #add
    thread = Thread(target = remove_add)
    thread.start()

    #functions
    thread = Thread(target = activate_functions)
    thread.start()

    wait(100,1) # random upstart

    #missions
    thread = Thread(target = missions)
    thread.start()

if __name__ == "__main__":
    main()
