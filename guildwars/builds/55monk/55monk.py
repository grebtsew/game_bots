import sys
import os
import time

# Lägg till två mappar upp i sökvägen
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from build_macro import start_click_schedule
from build_analyser import ClickSchedulePlotter


# List of (label, interval, effect_time, rest_time, cast_time, cost, priority, offset, init, doonce, req)
click_schedule = [
    {
        "key":"6",
        "interval":16,
        "effect_time":18,
        "rest_time":30,
        "cast_time":0,
        "cost":5,
        "priority":1,
        "offset":16,
        "init":True,
        "doonce":False,
        "req":1
    },
   {
         "key":"7",
        "interval":32,
        "effect_time":17,
        "rest_time":30,
        "cast_time":0,
        "cost":5,
        "priority":1,
        "offset":0,
        "init":True,
        "doonce":False,
        "req":1
    },
    {
        "key":"1",
        "interval":22,
        "effect_time":23,
        "rest_time":5,
        "cast_time":0.25,
        "cost":10,
        "priority":2,
        "offset":0,
        "init":True,
        "doonce":False,
        "req":2
    },
    {
        "key":"2",
        "interval":17.25,
        "effect_time":8,
        "rest_time":15,
        "cast_time":0.25,
        "cost":5,
        "priority":2,
        "offset":0,
        "init":True,
        "doonce":False,
        "req":3
    },
   {
        "key":"3",
        "interval":17.25,
        "effect_time":7,
        "rest_time":10,
        "cast_time":1,
        "cost":5,
        "priority":2,
        "offset":9.25,
        "init":True,
        "doonce":False,
        "req":3
    }  
]
  
    
if __name__=="__main__":

    # ANALYSE
    #plotter = ClickSchedulePlotter()
    #plotter.plot_schedule(click_schedule, sim_time=100)

    print("Starts in 2 seconds...")
    time.sleep(2)

    # RUN
    start_click_schedule(click_schedule)


    
    while True:
        time.sleep(1)