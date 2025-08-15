import threading
import time
from pynput.keyboard import Controller, Key
import pyautogui

# -------------------- Config --------------------

resource_pixel_start = (985, 1315)
resource_spacing = 18
resource_color = (93, 139, 181)

click_lock = threading.Lock()
resource_queue_lock = threading.Lock()
resource_condition = threading.Condition(resource_queue_lock)

waiting_queue = []

keyboard = Controller()

# -------------------- Functions --------------------

def get_resource_pixel_position(index):
    x = resource_pixel_start[0] + (index * resource_spacing)
    y = resource_pixel_start[1]
    return (x, y)

def check_visual_resources(cost):
    pixel_pos = get_resource_pixel_position(cost - 1)
    pixel_color = pyautogui.pixel(*pixel_pos)
    print(f"[CHECK] Resource check for cost {cost}: pixel {pixel_pos} = {pixel_color}")
    return pixel_color == resource_color

def wait_for_turn_and_resources(prio, thread_id, cost):
    with resource_condition:
        waiting_queue.append((prio, thread_id))
        while True:
            waiting_queue.sort()
            if waiting_queue[0] == (prio, thread_id) and check_visual_resources(cost):
                waiting_queue.pop(0)
                resource_condition.notify_all()
                return
            resource_condition.wait(timeout=0.2)

def press_key_with_lock(key_label, cast_time):
    with click_lock:
        key_obj = getattr(Key, key_label) if hasattr(Key, key_label) else key_label
        for _ in range(3):
            keyboard.press(key_obj)
            keyboard.release(key_obj)
        print(f"Pressed key '{key_label}' at {time.strftime('%X')}, cast time: {cast_time}s")
        time.sleep(cast_time)

def click_every_n_seconds(ability):
    """
    ability: dict med:
    key, interval, effect_time, rest_time, cast_time, cost, priority, offset, init, doonce, req
    """

    thread_id = threading.get_ident()
    key_label = ability["key"]
    interval = ability["interval"]
    cast_time = ability["cast_time"]
    
  
    cost = ability["cost"]
    prio = ability["priority"]
    offset = ability["offset"]
    init = ability["init"]
    doonce = ability["doonce"]

    now = time.time()
    if init:
        start_time = now + offset
    else:
        start_time = now + offset + interval

    while True:
        now = time.time()
        if now < start_time:
            time.sleep(start_time - now)

        wait_for_turn_and_resources(prio, thread_id, cost)
        press_key_with_lock(key_label, cast_time)

        
        

        if doonce:
            break

        start_time += interval

def start_click_schedule(schedule):

    # focus on screen
    pyautogui.click(x=100, y=100)

    for ability in schedule:
        t = threading.Thread(
            target=click_every_n_seconds,
            args=(ability,),
            daemon=True
        )
        t.start()
