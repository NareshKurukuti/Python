import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

win = tk.Tk()
win.title("scroll text")

#first label
label = ttk.Label(win, text='Enter a name: ')
label.grid(column=0, row=0)
label2 = ttk.Label(win, text='Choose a number: ').grid(column=1, row=0)

#textbox
name = tk.StringVar()
textbox = ttk.Entry(win, width=12, textvariable=name)
textbox.grid(column=0, row=1)

#combobox
number = tk.StringVar()
combobox = ttk.Combobox(win, width=12, textvariable=number)
combobox['values']=(1,2,3,4,5,6,7,8)
combobox.current(5)
combobox.grid(column=1, row=1)

colors = ['Blue', 'Gold', 'Red']

radvar = tk.IntVar()

def radcall():
    radsel = radvar.get()
    if radsel == 0: 
        win.configure(background=colors[0])
    elif radsel ==1:
        win.configure(background=colors[1])
    elif radsel == 2:
        win.configure(background=colors[2])

#radio button
for r in range(3):
    corerad = 'rad'+str(r)
    corerad = tk.Radiobutton(win, text=colors[r], variable=radvar, value=r, command=radcall)
    corerad.grid(column=r, row=3)










scrollW = 30
scrollH = 3

scr = scrolledtext.ScrolledText(win, width=scrollW, height=scrollH, wrap=tk.WORD)
scr.grid(column=0, columnspan = 2)


win.mainloop()
