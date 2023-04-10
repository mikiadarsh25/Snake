from tkinter import *
from tkinter.ttk import *
from time import strftime

window = Tk()
window.title("Clock")


def time():
    curTime = strftime('%H:%M:%S %p')
    label.config(text=curTime)
    label.after(1000,time)


label = Label(window,font=('ds-digital', 80), background='black', foreground='cyan')
label.pack(anchor='center')

time()
mainloop()
