import sys
import threading
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTextEdit, QLabel
from PyQt5.QtCore import QTimer, pyqtSignal, QObject
import pyautogui

# -------------------- Scheduler Config --------------------
box_size = 80
start_x = 1000
start_y = 1400
resource_pixel_start = (967, 1360)
resource_spacing = 18
resource_color = (24, 74, 121)

click_lock = threading.Lock()
resource_queue_lock = threading.Lock()
resource_condition = threading.Condition(resource_queue_lock)

waiting_queue = []
active = False

click_schedule = [
    ("1", 20, (start_x + 0 * box_size, start_y), 2, 10, 1),
    ("6", 14, (start_x + 5 * box_size, start_y), 2, 10, 2),
    ("2", 20, (start_x + 1 * box_size, start_y), 2, 5, 4),
    ("3", 23, (start_x + 2 * box_size, start_y), 2, 15, 3),
    ("4", 31, (start_x + 3 * box_size, start_y), 2, 10, 5),
    ("5", 20, (start_x + 4 * box_size, start_y), 2, 5, 6),
]

preset_schedule = [
    ("7", 20, (start_x + 6 * box_size, start_y), 2, 10, 8),
    ("8", 14, (start_x + 7 * box_size, start_y), 2, 10, 8),
    
]

# -------------------- Helper Functions --------------------
def get_resource_pixel_position(index):
    x = resource_pixel_start[0] + (index * resource_spacing)
    y = resource_pixel_start[1]
    return (x, y)

def check_visual_resources(cost):
    pixel_pos = get_resource_pixel_position(cost - 1)
    try:
        pixel_color = pyautogui.pixel(*pixel_pos)
    except:
        return False
    return pixel_color == resource_color

# -------------------- Worker Class --------------------
class ClickWorker(QObject):
    update_signal = pyqtSignal(str, list)

    def __init__(self):
        super().__init__()
        self.threads = []
        self.stop_flag = threading.Event()  # Use threading event for stopping threads

    def wait_for_turn_and_resources(self, prio, thread_id, cost):
        with resource_condition:
            waiting_queue.append((prio, thread_id))
            while True:
                waiting_queue.sort()
                if waiting_queue[0] == (prio, thread_id) and check_visual_resources(cost):
                    waiting_queue.pop(0)
                    resource_condition.notify_all()
                    return
                if self.stop_flag.is_set():  # Check for stop condition
                    return
                resource_condition.wait(timeout=0.2)

    def click_with_lock(self, label, coords, cast_time):
        global last_ran_label
        with click_lock:
            x, y = coords
            pyautogui.click(x, y)
            last_ran_label = label
            self.update_signal.emit(label, waiting_queue.copy())
            time.sleep(cast_time)

    def click_every_n_seconds(self, label, delay, coords, cast_time, cost, prio):
        thread_id = threading.get_ident()
        self.wait_for_turn_and_resources(prio, thread_id, cost)
        self.click_with_lock(label, coords, cast_time)

        if delay == 0 or self.stop_flag.is_set():
            return

        while not self.stop_flag.is_set():
            time.sleep(delay)
            self.wait_for_turn_and_resources(prio, thread_id, cost)
            self.click_with_lock(label, coords, cast_time)

    def start_schedule(self):
        global active
        active = True
        self.stop_flag.clear()  # Reset the stop flag
        for item in click_schedule:
            t = threading.Thread(target=self.click_every_n_seconds, args=item, daemon=True)
            t.start()
            self.threads.append(t)

    def stop_schedule(self):
        global active
        active = False
        self.stop_flag.set()  # Set the stop flag, stopping all running threads
        with resource_condition:
            waiting_queue.clear()
            resource_condition.notify_all()
        # Optionally, join threads here to ensure they're finished
        for t in self.threads:
            t.join()

    def run_preset_schedule(self):
        """ Runs the schedule items once (not looped). """
        for item in preset_schedule:
            if self.stop_flag.is_set():
                break  # If stop is requested, break out of the loop
            label, delay, coords, cast_time, cost, prio = item
            self.wait_for_turn_and_resources(prio, threading.get_ident(), cost)
            self.click_with_lock(label, coords, cast_time)
            

# -------------------- GUI Class --------------------
class SchedulerGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.worker = ClickWorker()

        self.init_ui()
        self.worker.update_signal.connect(self.update_display)

        self.timer = QTimer()
        self.timer.timeout.connect(self.refresh_display)
        self.timer.start(1000)

    def init_ui(self):
        self.setWindowTitle("Click Scheduler")
        self.setGeometry(200, 200, 400, 400)

        self.start_btn = QPushButton("Start")
        self.start_btn.clicked.connect(self.worker.start_schedule)

        self.stop_btn = QPushButton("Stop")
        self.stop_btn.clicked.connect(self.worker.stop_schedule)

        self.preset_btn = QPushButton("Run Preset")
        self.preset_btn.clicked.connect(self.worker.run_preset_schedule)

        self.queue_display = QTextEdit()
        self.queue_display.setReadOnly(True)

        self.last_clicked_label = QLabel("Last Clicked: None")

        layout = QVBoxLayout()
        layout.addWidget(self.start_btn)
        layout.addWidget(self.stop_btn)
        layout.addWidget(self.preset_btn)  # Add Preset button here
        layout.addWidget(self.last_clicked_label)
        layout.addWidget(self.queue_display)

        self.setLayout(layout)

    def update_display(self, last_label, queue):
        self.last_clicked_label.setText(f"Last Clicked: {last_label}")
        self.refresh_display()

    def refresh_display(self):
        display = "Current Queue (prio, thread_id):\n"
        with resource_queue_lock:
            for item in sorted(waiting_queue):
                display += f"{item}\n"
        self.queue_display.setPlainText(display)

# -------------------- App Entry --------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = SchedulerGUI()
    gui.show()
    sys.exit(app.exec_())
