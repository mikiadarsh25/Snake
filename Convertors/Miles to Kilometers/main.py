from tkinter import *

window = Tk()
window.title("Miles to Kilometer Convertor")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)
input = Entry()

input.grid(column=1, row=0)
mile = Label(text="miles")
mile.grid(column=2, row=0)


equal = Label(text="is equal to")
equal.grid(column=0, row=1)

output = Label(text="0")
output.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)


def on_click():
    an = int(input.get())
    kms = an * 1.609344
    output.config(text= kms)


button = Button(text="Calculate", command=on_click)
button.grid(column=1, row=2)

window.mainloop()
