import tkinter as tk
from tkinter import *

# Create a new window
root = tk.Tk()

# Create a Frame widget and pack it into the window
frame = tk.Frame(root)
frame.pack(side="left", fill="both", expand=True)

# Create a Canvas widget with a Scrollbar and pack it into the Frame
canvas = tk.Canvas(frame, borderwidth=0, highlightthickness=0)
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a scrollable Frame inside the Canvas and configure the Canvas to scroll it
scrollable_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=scrollable_frame)

for i in range(20):
    button = Button(frame, text )

if __name__ == "__main__":
    root.mainloop()