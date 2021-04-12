import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox

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








win.mainloop()
