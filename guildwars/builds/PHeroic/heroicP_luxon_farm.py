import random
from pynput.keyboard import Controller, Key
import time

import pyautogui

"""
Runs farm in Amatz Basin!
"""


keyboard = Controller()

states = [
    "idle",
    "fighting",
    "running"
]
x= 1410
y = 40

i = 0
max=7
stage=25
xp= 120
yp= 310
k=0
d=0
wanted_color=(119, 114, 91)
x_start = 120
y_start = 585


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

def press_key(key):
    print(f"Pressing {key}")
    keyboard.press(str(key))
    keyboard.release(str(key))

def fight():
    global i
    state="fighting"
    print(f"Current state: {state}")

    # start klick in case
    

    
    press_key(1)
    time.sleep(3+random.uniform(0,1))
    
    press_key(2)
    time.sleep(3+random.uniform(0,1))
    
    press_key(8)
    time.sleep(3+random.uniform(0,1))

    
    press_key(3)
    time.sleep(3+random.uniform(0,1))
    
    press_key(7)
    time.sleep(3+random.uniform(0,1))
    
    
    press_key(4)
    time.sleep(random.uniform(0,1))
        
    if i == max+1:
        i = 0

    print(f"Selecting player {i}")
    pyautogui.click(x=xp, y=yp+i*stage) # apply on ally
    i+=1
    press_key(5)
    time.sleep(2+random.uniform(0,1))
    
    press_key(5)
   

    
    press_key(6)


    
    state="idle"

    time.sleep(1+random.uniform(0, 2))



if __name__=="__main__":
    
    import time

    while True:
        
   

       
        print("fighting")
        while True:
         
            fight()
            
        # TODO: keep track of we are back in town