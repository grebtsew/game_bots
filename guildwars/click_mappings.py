import tkinter as tk
from screeninfo import get_monitors

# Example list: [(name, (x, y))]
points = [
    ("Player list Start", (120, 310)),
 ("Player2 ", (120, 310+25)),
 ("Resource Start ", (985, 1315)),
 ("Resource 2 ", (985+18, 1315)),
 ("Resource last ", (985+18*33, 1315)),
 ("Cost 5", (1057, 1315)),
 ("Begin challange",(120, 585)),
 ("target check",(1410,40))
]


# Get screen size (first monitor)
monitor = get_monitors()[0]
screen_width = monitor.width
screen_height = monitor.height

# Create transparent overlay window
root = tk.Tk()
root.overrideredirect(True)   # remove window borders
root.attributes("-topmost", True)
root.attributes("-transparentcolor", "black")  # black will be transparent
root.geometry(f"{screen_width}x{screen_height}+0+0")

canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg="black", highlightthickness=0)
canvas.pack()

# Draw points with names
for name, (x, y) in points:
    r = 5  # circle radius
    canvas.create_oval(x-r, y-r, x+r, y+r, fill="red", outline="white", width=2)
    canvas.create_text(x + 10, y, text=name, fill="yellow", anchor="w", font=("Arial", 12, "bold"))

root.mainloop()
