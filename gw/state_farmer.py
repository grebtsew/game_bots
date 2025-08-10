import random
from pynput.keyboard import Controller, Key
import time

import pyautogui

def get_pixel_color(x, y):
    """
    Returns the RGB color of the pixel at (x, y) on the screen.

    Parameters:
    - x: X-coordinate
    - y: Y-coordinate

    Returns:
    - (R, G, B): Tuple of RGB values
    """
    pixel_color = pyautogui.screenshot().getpixel((x, y))
    return pixel_color

def move_mouse_to(x, y, duration=0.2):
    """
    Moves the mouse to the specified screen coordinates.

    Parameters:
    - x: X-coordinate
    - y: Y-coordinate
    - duration: Time in seconds it takes to move (default 0.2s)
    """
    pyautogui.moveTo(x, y, duration=duration)

if __name__=="__main__":
    keyboard = Controller()

    states = [
        "idle",
        "fighting",
        "running"
    ]

    state = "idle"
    x= 1120
    y = 40
    
    i = 0
    max=7
    stage=33
    xp= 120
    yp= 310
    k=0
    d=0
    wanted_color=(180, 175, 152)
    print("Startar om 1 sekunder...")
    time.sleep(1)

    #move_mouse_to(xp,yp+7*stage)
    #print(get_pixel_color(x,y))
    # exit(0)
    try:
        while True:
            #print(get_pixel_color(x,y))
            #dprint(wanted_color)
            print(f"Current state: {state}")
            if (get_pixel_color(x,y)==wanted_color):
                d=0
                # target accessable
                keyboard.press(Key.space)
                keyboard.release(Key.space)
                state="fighting"
                keyboard.press('1')
                keyboard.release('1')
                time.sleep(random.uniform(0,1))
                
                keyboard.press('2')
                keyboard.release('2')
                time.sleep(random.uniform(0,1))
                
                keyboard.press('8')
                keyboard.release('8')
                time.sleep(random.uniform(0,1))


                keyboard.press('3')
                keyboard.release('3')
                time.sleep(random.uniform(0,1))
                
                keyboard.press('7')
                keyboard.release('7')
                time.sleep(random.uniform(0,1))
                
                
                keyboard.press('4')
                keyboard.release('4')
                time.sleep(random.uniform(0,1))
                 
                if i == max+1:
                    i = 0

                pyautogui.click(x=xp, y=yp+i*stage) # apply on ally
                i+=1
                keyboard.press('5')
                keyboard.release('5')
                time.sleep(2+random.uniform(0,1))
                
                keyboard.press('5')
                keyboard.release('5')
                pyautogui.click(x=x, y=y) # reset target
                move_mouse_to(1000,100)

                
                keyboard.press('6')
                keyboard.release('6')

            elif state=="idle":
                k+=1
                d+=1
                # try find new target
                keyboard.press(Key.tab)
                keyboard.release(Key.tab)
                time.sleep(0.2)
                keyboard.press(Key.space)
                keyboard.release(Key.space)
                if k > 2:
                    state="alone"
            elif state=="fighting":
                k = 0
                # try autoattack once
                keyboard.press(Key.space)
                keyboard.release(Key.space)
                state="idle"
            elif state=="alone":
                d+=1
                # Start running
                keyboard.press('r')
                keyboard.release('r')
                time.sleep(2+d+random.uniform(0, 1)    )
                # turn a little     R
                keyboard.press('d')
                time.sleep(0.1+random.uniform(0, 1)) 
                keyboard.release('d')
                
                state="idle"

            time.sleep(1+random.uniform(0, 2))
              
    except KeyboardInterrupt:
        print("Avslutat av användaren.")
                         