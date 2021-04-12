import tkinter as tk
from tkinter import ttk
from sys import argv, exit

if argv[1:]:
    file_name = argv[1]
    file_name2 = argv[2]
    with open(file_name) as file:
        f = file.read()
else:
    print("please enter filename at start program")
    exit(0)

win = tk.Tk()
win.title("copy....")
aLabel = ttk.Label(win, text="copy {} to {}".format(file_name, file_name2))
aLabel.grid(column=0, row=0)

def Copy():
    try:
        f2 = open(file_name2, 'w')
        action.configure(f2.write(f))
        aLabel.configure(foreground='red')
        f2.close()
    except TypeError:
        print('Ok!')
        exit(0)
action = ttk.Button(win, text='click to copy',command=Copy)
action.grid(column=1, row=0)
win.mainloop()
