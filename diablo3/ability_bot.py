import math
import pyautogui
import sys
import keyboard
from threading import Thread

sys.path.append("..")

import core_bot as bot

'''
This program helps with activating abilities for you.
Helpful if you only can use one hand while gaming.
For each build you will need change the cooldowns below
This program will press 1,2,3,4 and right button for you
'''

cooldown_rc = 5; # right click
cooldown_1 = 0.51234;
cooldown_2 = 2;
cooldown_3 = 100;
cooldown_4 = 3;

def right_click(delay):
    while bot.bot_running:
        pyautogui.click(button='right')
        #print("pressed right")
        bot.wait(delay, 0.1)

def ability(value):
    keyboard.press_and_release(value)
    #print("pressed " +value)

def run(abi, delay):
    while bot.bot_running:
        ability(abi)
        bot.wait(delay, 0.1)

def main():
    thread = Thread(target=bot.hook, args=(None,))
    thread.start()
    thread = Thread(target=right_click, args=(cooldown_rc,))
    thread.start()
    thread = Thread(target=run, args=('1',cooldown_1,))
    thread.start()
    thread = Thread(target=run, args=('2',cooldown_2,))
    thread.start()
    thread = Thread(target=run, args=('3',cooldown_3,))
    thread.start()
    thread = Thread(target=run, args=('4',cooldown_4,))
    thread.start()

if __name__ == "__main__":
    main()
