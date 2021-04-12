import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import scrolledtext

win = tk.Tk()
win.title('Python GUI')

def msgbox():
    mBox.showinfo('Python is the Best', 'this is msgbox')

def msgbox2():
    mBox.showwarning('', 'this is warning')

def msgError():
    mBox.showerror('Python error', 'a python gui using tkinter \n Error')

def msgbox4():
    answer = mBox.askyesno('python message dual choice Box', 'Are You Sure')
    print(answer)

    
menubar = Menu(win)
win.configure(menu=menubar)

filemenu = Menu(menubar, tearoff=0)
helpmenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='New') 
helpmenu.add_command(label='About', command=msgbox)
helpmenu.add_command(label='Warning', command=msgbox2)
helpmenu.add_command(label='Error', command=msgError)
helpmenu.add_command(label='YesNo', command=msgbox4)

menubar.add_cascade(label='Help', menu=helpmenu)
menubar.add_cascade(label='File', menu=filemenu)


def _spin():
    value = spin.get()
    print(value)
    scr.insert(tk.INSERT, value + '\n')


    
spin=tk.Spinbox(win, from_=0, to=10, width=10,bd=8, command=_spin)
spin.grid(column=0, row=0)
scr = scrolledtext.ScrolledText(win, width=30, height=3, wrap=tk.WORD)
scr.grid(column=0, row=1, sticky='WE', columnspan=3)








win.mainloop()
