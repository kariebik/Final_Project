from tkinter import *
# line1 imports every thing from the tkinter file

window = Tk()
# creates a window

window.title("Calculator app")
# gives window a name

e = Entry(window, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


window.mainloop()