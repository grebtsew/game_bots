import random
from pynput.keyboard import Controller, Key
import time
import pyautogui

"""
Maintain Heroic refrain 
"""


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

    i = 0
    max=7
    stage=25
    xp= 120
    yp= 310
 
    print("Startar om 1 sekunder...")
    time.sleep(1)

   
    try:
        while True:

                if i == max+1:
                    i = 0
                print(f"Apply heroic refrain on player {i}")
                pyautogui.click(x=xp, y=yp+i*stage) # apply on ally
                i+=1
                keyboard.press('5')
                keyboard.release('5')
                time.sleep(1+random.uniform(0,1))
                
                time.sleep(15)
              
    except KeyboardInterrupt:
        print("Avslutat av användaren.")
                         