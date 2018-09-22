import math
import pyautogui
import sys
import keyboard
sys.path.append("..")

import core_bot as bot

'''
This program helps with controlling the character in diablo3
With this program you can walk with the arrow buttons on keyboard.
This is great if you don't have any mouse available!
'''
WINDOW = bot.WINDOW_SIZE_STRUCT()
WINDOW.x = 1920
WINDOW.y = 1080

charpos_x = 900
charpos_y = 540
radius = 120

def main():
    thread = Thread(target=bot.hook, args=(None,))
    thread.start()


    while bot.bot_running:
        angle = 0
        pressed = False

        if(keyboard.is_pressed('ctrl')):
            radius = 200
        else:
            radius = 150

        if(keyboard.is_pressed('left')):
            pressed = True
            angle = math.pi
        if(keyboard.is_pressed('up')):
            pressed = True
            angle = (math.pi*3)/2
        if(keyboard.is_pressed('down')):
            angle = math.pi/2
            pressed = True
        if(keyboard.is_pressed('right')):
            angle = 0
            pressed = True

        if(keyboard.is_pressed('down') and keyboard.is_pressed('left')):
            angle = math.pi*3/4
        if(keyboard.is_pressed('down') and keyboard.is_pressed('right')):
            angle = math.pi/4
        if(keyboard.is_pressed('up') and keyboard.is_pressed('left')):
            angle = math.pi*5/4
        if(keyboard.is_pressed('up') and keyboard.is_pressed('right')):
            angle = math.pi*7/4

        #click
        if pressed:
            pyautogui.click(charpos_x + (radius * math.cos(angle)), charpos_y + (radius * math.sin(angle)))
            bot.wait(0.1,0.1)

if __name__ == "__main__":
    main()
