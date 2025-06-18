import tkinter as tk
from tkinter import ttk, font

root = tk.Tk()
root.title("Fonts")
root.geometry("500x500")

canvas = tk.Canvas(root)
scrollframe = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollframe.set)

scrollframe.pack_configure(side="right", fill="y")
canvas.pack_configure(side="left", fill="both", expand=True)

# Create frame inside canvas
frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")


# Update scrollregion when frame changes
def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))


frame.bind("<Configure>", on_configure)

for font in font.families():
    ttk.Label(frame, text=f"xray and zebra in {font}", font=(font, 18)).pack()


root.mainloop()

import tkinter as tk
from tkinter import ttk, font

root = tk.Tk()
root.title("Fonts")
root.geometry("500x500")

canvas = tk.Canvas(root)
scrollframe = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollframe.set)

scrollframe.pack_configure(side="right", fill="y")
canvas.pack_configure(side="left", fill="both", expand=True)

# Create frame inside canvas
frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")


# Update scrollregion when frame changes
def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))


frame.bind("<Configure>", on_configure)

for font in font.families():
    ttk.Label(frame, text=f"xray and zebra in {font}", font=(font, 18)).pack()


root.mainloop()

