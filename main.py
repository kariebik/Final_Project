from tkinter import *  # line1 imports every thing from the tkinter file
import math

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

# defines the buttons
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
button_sin = Button(window, text='sin', padx=40, pady=20, command= lambda: click_button('sin'))
button_cos = Button(window, text='cos', padx=40, pady=20, command= lambda: click_button('cos'))
button_tan = Button(window, text='tan', padx=40, pady=20, command= lambda: click_button('tan'))
clear_button = Button(window, text='Clear', padx=90, pady=20, command= clear_button)

button1.grid(row=3, column=0)  # This places button within the window at a specified place
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row= 2, column=1)
button6.grid(row= 2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
button_sin.grid(row=1, column=3)
button_cos.grid(row=2, column=3)
button_tan.grid(row=3, column=3)
clear_button.grid(row=4, column=1, columnspan=2)


def add_button():
    """
    This is the function for the add button. It save the value on the calculator and tells the equals button how to react
    :return:
    """
    first_number = e.get()
    global f_num
    global symbol
    f_num = eval(first_number)
    e.delete(0, END)
    symbol = "+"

def equals_button():
    """
    This is the command for the equals button. Its action changes depending on the value of symbol to know how to react to the previous button.
    :return:
    """
    if symbol == "+":
        second_number = eval(e.get())
        e.delete(0, END)
        e.insert(0, str(f_num + second_number))

def sqrt_button(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + num)

button_sqrt = Button(window, text='√', padx=40, pady=20, command= lambda: click_button("√"))
button_sqrt.grid(row=1, column=5)

button_add = Button(window, text='+', padx=40, pady=20, command= add_button)
button_add.grid(row=5, column=0)

eq_button = Button(window, text='=', padx=100, pady=20, command= equals_button)
eq_button.grid(row=5, column=1, columnspan=2)

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
def main():
    global result
    text = e.get()
    operation = text[0:3]
    angle = int(text[3: -1])
    if operation == "sin":
        result = math.sin(angle)
    elif operation == "cos":
        result = math.cos(angle)
    elif operation == "tan":
        result = math.tan(angle)
    e.delete(0, END)
    e.insert(0, str(result)) c

window.mainloop()
