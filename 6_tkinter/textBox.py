import tkinter as tk
from tkinter import ttk


win = tk.Tk()
win.title('Python tkinter')

aLabel = ttk.Label(win, text="Enter a name: ")
aLabel.grid(column=0, row=0)


def clickMe():
    if name.get():
        action.configure(text='Hello '+ name.get())
        aLabel.configure(foreground='green')

action = ttk.Button(win, text="click me", command=clickMe)
action.grid(column=1, row=1)

name = tk.StringVar()

textbox = ttk.Entry(win, width=12, textvariable=name)
textbox.grid(column=0, row=1)


win.mainloop()
