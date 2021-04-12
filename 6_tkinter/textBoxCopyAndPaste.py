import tkinter as tk
from tkinter import ttk


win = tk.Tk()
win.title('copy ...... past')

aLabel = ttk.Label(win, text="Enter a file name: ")
aLabel.grid(column=0, row=0)


def clickMe():
    try:
        file_name = name.get()
        with open(file_name) as file:
            f1 = file.read()
        file_name2 = name2.get()
        f2 = open(file_name2, 'w')
        aLabel.configure(foreground='green')
        action.configure(text='Copied')
        f2.close()

    except:
        action.configure(text='Ok ! file has been write')
        with open(file_name2) as file:
            f2 = file.read()
        action.configure(text=f2)
        

action = ttk.Button(win, text="click to copy", command=clickMe)
action.grid(column=1, row=1)

name = tk.StringVar()
name2 = tk.StringVar()

textbox = ttk.Entry(win, width=12, textvariable=name)
textbox.grid(column=0, row=1)
textbox = ttk.Entry(win, width=12, textvariable=name2).grid(column=0, row=2)


win.mainloop()
