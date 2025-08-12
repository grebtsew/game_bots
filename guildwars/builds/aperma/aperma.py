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

# Priority queue: (prio, thread_id)
waiting_queue = []

# List of (label, interval, coords, cast_time, cost, priority)
click_schedule = [
    ("5", 19, (start_x + 4 * box_size, start_y), 2, 1, 1),
    ("1", 20, (start_x + 0 * box_size, start_y), 0.5, 15, 2),
    ("2", 20, (start_x + 1 * box_size, start_y), 0.5, 5, 3),
    ("3", 60, (start_x + 2 * box_size, start_y), 2, 10, 4),
    ("4", 32, (start_x + 3 * box_size, start_y), 2, 5, 5),
    ("6", 32, (start_x + 5 * box_size, start_y), 2, 10, 6),
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
            # Sort queue by priority (lowest number = highest priority)
            waiting_queue.sort()
            if waiting_queue[0] == (prio, thread_id) and check_visual_resources(cost):
                waiting_queue.pop(0)
                resource_condition.notify_all()
                return
            resource_condition.wait(timeout=0.2)

def click_with_lock(label, coords, cast_time):
    with click_lock:
        x, y = coords
        pyautogui.click(x, y)
        print(f"Clicked '{label}' at ({x}, {y}) at {time.strftime('%X')}, cast time: {cast_time}s")
        time.sleep(cast_time)

def click_every_n_seconds(label, delay, coords, cast_time, cost, prio):
    thread_id = threading.get_ident()
    # Initial castsm
    wait_for_turn_and_resources(prio, thread_id, cost)
    click_with_lock(label, coords, cast_time)

    if delay == 0:
        return

    while True:
        time.sleep(delay)
        wait_for_turn_and_resources(prio, thread_id, cost)
        click_with_lock(label, coords, cast_time)

def start_click_schedule(schedule):
    for (label, delay, coords, cast_time, cost, prio) in schedule:
        t = threading.Thread(
            target=click_every_n_seconds,
            args=(label, delay, coords, cast_time, cost, prio),
            daemon=True
        )
        t.start()

# -------------------- Main --------------------
if __name__ == "__main__":
    print("Starting prioritized pixel-based resource scheduler. Press Ctrl+C to stop.")
    start_click_schedule(click_schedule)

    #(x,y)=get_resource_pixel_position(0)
    #pyautogui.click(x, y)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nScript stopped by user.")
