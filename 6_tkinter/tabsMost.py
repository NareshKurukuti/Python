import tkinter as tk
from tkinter import ttk
from sys import exit
from tkinter import Menu

win = tk.Tk()
win.title('python GUI TAB')

tabs = ttk.Notebook(win)

tab1 = ttk.Frame(tabs)

tabs.add(tab1, text='Tab 1')
tabs.pack()

monty = ttk.LabelFrame(tab1, text='Monty Python')
monty.grid(column=0, row=0, sticky='WE')
label1=ttk.Label(monty, text='Enter a Name')
label1.grid(column=0, row=0)

name=tk.StringVar();
textb=ttk.Entry(monty, width=12, textvariable=name)
textb.grid(column=0, row=1)


tab2 = ttk.Frame(tabs)
tabs.add(tab2, text='Tab 2')

monty2 = ttk.LabelFrame(tab2, text='Monty Python2')
monty2.grid(column=0, row=0, sticky='WE')
label2 = ttk.Label(monty2, text='Choose a number')
label2.grid(column=0, row=0)

name2=tk.StringVar()
combob=ttk.Combobox(monty2, width=12, textvariable=name2)
combob.grid(column=0, row=1)
combob['values']=(1,2,3,4,5,6,7,9)
combob.current(2)
tabs.pack()


def exitt():
    exit(0)





#file menu
menubar = Menu(win)
win.config(menu=menubar)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='New File')
filemenu.add_command(label='New Window')
menubar.add_cascade(label='File', menu=filemenu)

#help menu
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label='About')
helpmenu.add_command(label='Exit', command=exitt)
helpmenu.add_command(label='Welcome')
menubar.add_cascade(label='Help', menu=helpmenu)










win.mainloop()
