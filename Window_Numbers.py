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

def clear_button():
    """
    This is the command for the clear button
    It empties e (the entry space on the window)
    :return:
    """
    e.delete(0, END)

button1 = Button(window, text='1', padx=40, pady=20, command= lambda: click_button('1'))
button2 = Button(window, text='2', padx=40, pady=20, command= lambda: click_button('2'))
button3 = Button(window, text='3', padx=40, pady=20, command= lambda: click_button('3'))
button4 = Button(window, text='4', padx=40, pady=20, command= lambda: click_button('4'))
button5 = Button(window, text='5', padx=40, pady=20, command= lambda: click_button('5'))
button6 = Button(window, text='6', padx=40, pady=20, command= lambda: click_button('6'))
button7 = Button(window, text='7', padx=40, pady=20, command= lambda: click_button('7'))
button8 = Button(window, text='8', padx=40, pady=20, command= lambda: click_button('8'))
button9 = Button(window, text='9', padx=40, pady=20, command= lambda: click_button('9'))
button0 = Button(window, text='0', padx=40, pady=20, command= lambda: click_button('0'))
clear_button = Button(window, text='Clear', padx=90, pady=20, command= clear_button)


# defines the buttons
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row= 2, column=1)
button6.grid(row= 2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
clear_button.grid(row=4, column=1, columnspan=2)

def add_button():
    first_number = e.get()
    global f_num
    global symbol
    f_num = eval(first_number)
    e.delete(0, END)
    symbol = "+"

def equals_button():
    if symbol == "+":
        second_number = eval(e.get())
        e.delete(0, END)
        e.insert(0, str(f_num + second_number))


button_add = Button(window, text='+', padx=40, pady=20, command= add_button)
button_add.grid(row=5, column=0)

eq_button = Button(window, text='=', padx=100, pady=20, command= equals_button)
eq_button.grid(row=5, column=1, columnspan=2)

window.mainloop()