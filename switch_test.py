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

button1 = Button(window, text='1', padx=40, pady=20, command= lambda: click_button('1'))
button2 = Button(window, text='2', padx=40, pady=20, command= lambda: click_button('2'))



def switch_button():
    button1.grid_remove()
    button2.grid(row=3, column=0)
    shift.grid_remove()
    shift2.grid(row=3, column=1)


def switch_button2():
    button2.grid_remove()
    button1.grid(row=3, column=0)
    shift2.grid_remove()
    shift.grid(row=3, column=1)

shift = Button(window, text= 'shift', padx=40, pady=20, command= switch_button)
shift2 = Button(window, text= 'shift', padx=40, pady=20, command= switch_button2)

shift.grid(row=3, column=1)
button1.grid(row=3, column=0)

button_pi = Button(window, text='π', padx=40, pady=20, command= lambda: click_button('π'))
button_pi.grid(row=3, column=2)
window.mainloop()