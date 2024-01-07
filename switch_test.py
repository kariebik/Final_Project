from tkinter import *  # line1 imports every thing from the tkinter file

window = Tk()  # creates a window

window.title("Calculator app")  # gives window a name

e = Entry(window, width=35, borderwidth=5)  # This creates a place for the user to enter values
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)  # This places e within the window at a specified place

def click_button(num):
    """
    This function will act as the command for multiple buttons and allows the user to input values using button
    :param num: the symbol associated with said button
    :return: inserts the symbol with previous text
    """
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + num)

import math


button_pi = Button(window, text='π', padx=40, pady=20, command= lambda: click_button(str(math.pi)))
button_pi.grid(row=1, column=4)

button_e = Button(window, text='e', padx=40, pady=20, command= lambda: click_button(str(math.e)))
def switch_button():
    button_pi.grid_remove()
    button_e.grid(row=1, column=4)
    shift.grid_remove()
    shift2.grid(row=2, column=4)


def switch_button2():
    button_e.grid_remove()
    button_pi.grid(row=1, column=4)
    shift2.grid_remove()
    shift.grid(row=2, column=4)

shift = Button(window, text= 'shift', padx=40, pady=20, command= switch_button)
shift2 = Button(window, text= 'shift', padx=40, pady=20, command= switch_button2)

shift.grid(row=2, column=4)
window.mainloop()