import pyautogui
import threading
import time

# -------------------- Config --------------------
box_size = 80
start_x = 1000
start_y = 1400

# Pixel-based resource check
resource_pixel_start = (985, 1360)
resource_spacing = 18
resource_color = (24, 74, 121)

# Global locks
click_lock = threading.Lock()
resource_queue_lock = threading.Lock()
resource_condition = threading.Condition(resource_queue_lock)

# Priority queue: (prio, thread_id)ssssss
waiting_queue = []

# List of (label, interval, coords, cast_time, cost, priority, offset, init)
click_schedule = [
    ("6", 15, (start_x + 5 * box_size, start_y), 0, 5, 1, 15, False),
    ("7", 30, (start_x + 6 * box_size, start_y), 0, 5, 1, 0, True),
    ("1", 22, (start_x + 0 * box_size, start_y), 0, 10, 2, 0, True),
    ("2", 15.25, (start_x + 1 * box_size, start_y), 0, 5, 2, 0, True),
    ("3", 4.1, (start_x + 2 * box_size, start_y), 2, 5, 2, 9, False),
   
]
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
            # Sort queue by priority (lowesti number = highest priority)
            waiting_queue.sort()
            if waiting_queue[0] == (prio, thread_id) and check_visual_resources(cost):
                waiting_queue.pop(0)
                resource_condition.notify_all()
                return
            resource_condition.wait(timeout=0.2)

def click_with_lock(label, coords, cast_time):
    try:
        with click_lock:
            x, y = coords
            pyautogui.click(x, y)
            pyautogui.click(x, y)
            pyautogui.click(x, y)
            print(f"Clicked '{label}' at ({x}, {y}) at {time.strftime('%X')}, cast time: {cast_time}s")
            time.sleep(cast_time)
    except Exception as e:
        print(str(e))

def click_every_n_seconds(label, delay, coords, cast_time, cost, prio,offset,init):
    thread_id = threading.get_ident()
    # Initial castsm
    if init:
        wait_for_turn_and_resources(prio, thread_id, cost)
        click_with_lock(label, coords, cast_time)

    if delay == 0:
        return

    while True:
        if offset != 0:
            time.sleep(offset)
            wait_for_turn_and_resources(prio, thread_id, cost)
            click_with_lock(label, coords, cast_time)
        time.sleep(delay)
        wait_for_turn_and_resources(prio, thread_id, cost)
        click_with_lock(label, coords, cast_time)

def start_click_schedule(schedule):
    for (label, delay, coords, cast_time, cost, prio,offset,init) in schedule:
        t = threading.Thread(
            target=click_every_n_seconds,
            args=(label, delay, coords, cast_time, cost, prio,offset,init),
            daemon=True
        )
        t.start()

# -------------------- Main --------------------
if __name__ == "__main__":
    print("Starting prioritized pixel-based resource scheduler. Press Ctrl+C to stop.")
    start_click_schedule(click_schedule)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nScript stopped by user.")
