import tkinter as tk
from tkinter import ttk


win = tk.Tk()

win.title("Python  GUI")

win.resizable(0,0)

aLabel = ttk.Label(win, text='A Label!')
aLabel.grid(column=0, row=0)
#ttk.Label(win, text='A Label!').grid(column=0, row=0)


def clickMe():
    action.configure(text='** i have been clicked!!!')
    aLabel.configure(foreground='red')





action = ttk.Button(win, text='clik me', command=clickMe)
action.grid(column=1, row=0) 
win.mainloop()
