

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
        "key":"1",
        "interval":24,
        "effect_time":15,
        "rest_time":10,
        "cast_time":1,
        "cost":5,
        "priority":1,
        "offset":0,
        "init":True,
        "doonce":False,
        "req":1
    },
   {
         "key":"2",
        "interval":24,
        "effect_time":22,
        "rest_time":30,
        "cast_time":1,
        "cost":5,
        "priority":1,
        "offset":2,
        "init":True,
        "doonce":False,
        "req":2
    },
    
     {
        "key":"3",
        "interval":24,
        "effect_time":9,
        "rest_time":30,
        "cast_time":1,
        "cost":10,
        "priority":2,
        "offset":4,
        "init":True,
        "doonce":False,
        "req":5
    }  ,
   {
        "key":"4",
        "interval":24,
        "effect_time":33,
        "rest_time":10,
        "cast_time":1,
        "cost":5,
        "priority":2,
        "offset":6,
        "init":True,
        "doonce":False,
        "req":4
    }  ,
    {
        "key":"7",
        "interval":24,
        "effect_time":62,
        "rest_time":45,
        "cast_time":1,
        "cost":10,
        "priority":2,
        "offset":18,
        "init":True,
        "doonce":False,
        "req":3
    },{
        "key":"5",
        "interval":48,
        "effect_time":62,
        "rest_time":45,
        "cast_time":1,
        "cost":10,
        "priority":2,
        "offset":20,
        "init":True,
        "doonce":False,
        "req":3
    },
    {
        "key":"6",
        "interval":24,
        "effect_time":62,
        "rest_time":45,
        "cast_time":1,
        "cost":10,
        "priority":2,
        "offset":22,
        "init":True,
        "doonce":False,
        "req":3
    }
    
]

"""

,
    {
        "key":"4",
        "interval":30,
        "effect_time":10,
        "rest_time":30,
        "cast_time":0.25,
        "cost":5,
        "priority":2,
        "offset":0,
        "init":True,
        "doonce":False,
        "req":3
    }

  
   {
        "key":"7",
        "interval":15,
        "effect_time":5,
        "rest_time":5,
        "cast_time":0.25,
        "cost":5,
        "priority":2,
        "offset":9.25,
        "init":True,
        "doonce":False,
        "req":6
    } ,
   {
        "key":"8",
        "interval":60,
        "effect_time":54,
        "rest_time":20,
        "cast_time":0.25,
        "cost":5,
        "priority":2,
        "offset":9.25,
        "init":True,
        "doonce":False,
        "req":7
    }
    """
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