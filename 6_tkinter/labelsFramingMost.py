import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from sys import exit

win =tk.Tk()
win.title("python frames")


"""Eample One For Label Frames """

labelsFrames = ttk.LabelFrame(win, text='Lables in a frame')
labelsFrames.grid(column=0, row=0, padx = 20, pady = 20)

"""
#place labels into the container

ttk.Label(labelsFrames, text='Label 1').grid(column=0, row=0)
ttk.Label(labelsFrames, text='Label 2').grid(column=0, row=1)
ttk.Label(labelsFrames, text='Label 3').grid(column=0, row=2)
ttk.Label(labelsFrames, text='Label 4').grid(column=0, row=3)
ttk.Label(labelsFrames, text='Label 5').grid(column=0, row=4)
ttk.Label(labelsFrames, text='Label 6').grid(column=0, row=5)
ttk.Label(labelsFrames, text='Label 7').grid(column=0, row=6)
ttk.Label(labelsFrames, text='Label 8').grid(column=0, row=7)


for c in labelsFrames.winfo_children():
    c.grid_configure(padx=8, pady=4)
"""


"""Example Two"""

monty = ttk.LabelFrame(win, text=' Monty Python ')
monty.grid(column=0, row=0)

#first label
label1 = ttk.Label(monty, text='Enter a name: ')
label1.grid(column=0, row=0)

#textbox
name = tk.StringVar()
textb = ttk.Entry(monty, width=12, textvariable = name)
textb.grid(column=0, row=1)
textb.focus()

#second label
label2 = ttk.Label(monty, text="Choose a number: ")
label2.grid(column=1, row=0)

#combobox
number = tk.StringVar()
cbox = ttk.Combobox(monty, width=12, textvariable=number)
cbox['values']=(1,2,3,4,5,6)
cbox.current(0)
cbox.grid(column=1, row=1)

def clickMe():
    if chvar1.get() ==1:
        label1.configure(foreground='green')
    elif chvar1.get()==0:
        label1.configure(foreground='black')
    if chvar2.get() ==1:
        label2.configure(foreground='gold')
    elif chvar2.get() ==0:
        label2.configure(foreground='black')

#button
action = ttk.Button(monty, text='Click Me', command=clickMe)
action.grid(column=2, row=1)

#checkbox
chvar1 = tk.IntVar()
checkB1 = tk.Checkbutton(monty, text='Disable', variable=chvar1, command=clickMe)
checkB1.grid(column=0, row=2)
chvar2 = tk.IntVar()
checkB2 = tk.Checkbutton(monty, text='Unchecked', variable=chvar2, command=clickMe)
checkB2.grid(column=1, row=2)
chvar3 = tk.IntVar()
checkB3 = tk.Checkbutton(monty, text='togg', variable=chvar3, command=clickMe)
checkB3.grid(column=2, row=2)

#scrolledText
scr = scrolledtext.ScrolledText(monty, width=30, height=3, wrap=tk.WORD)
scr.grid(column=0, sticky='WE', columnspan=3)


monty2 = ttk.LabelFrame(win, text='Monty Python2')
monty2.grid(column=0, row=1, sticky = 'WE')

label3 = ttk.Label(monty2, text='Choose an option').grid(column=0, row=0)
chvar = tk.IntVar()

color = ['Blue', 'Gold', 'Red']
for i in range(3):
    rB = 'rB'+ str(i)
    rB = tk.Radiobutton(monty2, text=color[i], variable=chvar, value=i)
    rB.grid(column=i, row=1)
    
def exitt():
    exit(0)


"""Example Menu's """

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
