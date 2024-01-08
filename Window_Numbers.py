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

import math
def log_button():
    global f_num
    f_num = eval(e.get())
    result = math.log10(f_num)
    e.delete(0, END)
    e.insert(0, str(result))

button_log = Button(window, text='log', padx=40, pady=20, command=log_button)
button_log.grid(row=1, column=4)

button_pi = Button(window, text='π', padx=40, pady=20, command= lambda: click_button(str(math.pi)))
button_pi.grid(row=1, column=4)

window.mainloop()

x=int(input("please emter number of your mom)")
def logx_button():
    global f_num
    f_num = eval(e.get())
    result = math.logx(f_num)
    e.delete(0, END)
    e.insert(0, str(result))

button_logx = Button(window, text='logx', padx=40, pady=20, command=logx_button)
button_logx.grid(row=1, column=5)

def solve_quadratic():
    a = float(e.get())
    b = float(e.get())
    c = float(e.get())

    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        messagebox.showinfo("Solution", "No real solutions.")
    elif discriminant == 0:
        solution = -b / (2*a)
        messagebox.showinfo("Solution", f"One real solution: {solution}")
    else:
        solution1 = (-b + math.sqrt(discriminant)) / (2*a)
        solution2 = (-b - math.sqrt(discriminant)) / (2*a)
        messagebox.showinfo("Solution", f"Two real solutions: {solution1} and {solution2}")

def solve_cubic():
    # Add your code to solve cubic equations here
    pass

# Define buttons
button1 = Button(window, text='1', padx=40, pady=20, command=lambda: click_button(1))
button2 = Button(window, text='2', padx=40, pady=20, command=lambda: click_button(2))
button3 = Button(window, text='3', padx=40, pady=20, command=lambda: click_button(3))
button4 = Button(window, text='4', padx=40, pady=20, command=lambda: click_button(4))
button5 = Button(window, text='5', padx=40, pady=20, command=lambda: click_button(5))
button6 = Button(window, text='6', padx=40, pady=20, command=lambda: click_button(6))
button7 = Button(window, text='7', padx=40, pady=20, command=lambda: click_button(7))
button8 = Button(window, text='8', padx=40, pady=20, command=lambda: click_button(8))
button9 = Button(window, text='9', padx=40, pady=20, command=lambda: click_button(9))
button0 = Button(window, text='0', padx=40, pady=20, command=lambda: click_button(0))
button_sin = Button(window, text='sin', padx=40, pady=20, command=lambda: click_button('sin'))
button_cos = Button(window, text='cos', padx=40, pady=20, command=lambda: click_button('cos'))
button_tan = Button(window, text='tan', padx=40, pady=20, command=lambda: click_button('tan'))
button_log = Button(window, text='log', padx=40, pady=20, command=log_button)
solver_button = Button(window, text='Solver', padx=40, pady=20, command=solver_button)
clear_button = Button(window, text='Clear', padx=90, pady=20, command=clear_button)
button_add = Button(window, text='+', padx=40, pady=20, command=add_button)

buttons = [
    (button1, 3, 0), (button2, 3, 1), (button3, 3, 2), (button4, 2, 0),
    (button5, 2, 1), (button6, 2, 2), (button7, 1, 0), (button8, 1, 1),
    (button9, 1, 2), (button0, 4, 0), (button_sin, 1, 3), (button_cos, 2, 3),
    (button_tan, 3, 3), (button_log, 4, 1), (solver_button, 4, 2), (button_add, 5, 0)
]

for (button, row, col) in buttons:
    button.grid(row=row, column=col)

eq_button = Button(window, text='=', padx=100, pady=20, command=solve_equation)
eq_button.grid(row=5, column=1, columnspan=2)
 def factorial_button():
    num = int(e.get())
    result = math.factorial(num)
    e.delete(0, END)
    e.insert(0, str(result))
# def solve_cubic(a, b, c, d):
#     # Cubic equation: ax^3 + bx^2 + cx + d = 0
#
#     # Substitute x = y - b/(3a) to eliminate the quadratic term
#     p = (3*a*c - b**2) / (3*a**2)
#     q = (2*b**3 - 9*a*b*c + 27*a**2*d) / (27*a**3)
#
#     # Calculate discriminant
#     delta = (q/2)**2 + (p/3)**3
#
#     # Calculate complex cube roots
#     sqrt_delta = (-1)**0.5 * delta
#     u1 = (q/2 + sqrt_delta)**(1/3)
#     u2 = (q/2 - sqrt_delta)**(1/3)
#
#     # Calculate real roots
#     y1 = u1 + u2 - b / (3*a)
#     y2 = -(u1 + u2) / 2 - b / (3*a) + (u1 - u2) * (3**0.5) / 2j
#     y3 = -(u1 + u2) / 2 - b / (3*a) - (u1 - u2) * (3**0.5) / 2j
#
#     return y1, y2, y3
#
# # Example
# a = float(input("Enter the coefficient a: "))
# b = float(input("Enter the coefficient b: "))
# c = float(input("Enter the coefficient c: "))
# d = float(input("Enter the coefficient d: "))
#
# solutions = solve_cubic(a, b, c, d)
#
# print(f"Solutions for the cubic equation: {solutions}")

# import math
#
# def solve_quadratic(a, b, c):
#     # Quadratic equation: ax^2 + bx + c = 0
#
#     # Calculate the discriminant
#     discriminant = b**2 - 4*a*c
#
#     # Check the nature of roots based on the discriminant
#     if discriminant > 0:
#         # Two distinct real roots
#         root1 = (-b + math.sqrt(discriminant)) / (2*a)
#         root2 = (-b - math.sqrt(discriminant)) / (2*a)
#         return root1, root2
#     elif discriminant == 0:
#         # One real root (double root)
#         root = -b / (2*a)
#         return root,
#     else:
#         # Complex conjugate roots
#         real_part = -b / (2*a)
#         imag_part = math.sqrt(abs(discriminant)) / (2*a)
#         root1 = complex(real_part, imag_part)
#         root2 = complex(real_part, -imag_part)
#         return root1, root2
#
# # Example
# a = float(input("Enter the coefficient a: "))
# b = float(input("Enter the coefficient b: "))
# c = float(input("Enter the coefficient c: "))
#
# solutions = solve_quadratic(a, b, c)
#
# print(f"Solutions for the quadratic equation: {solutions}")
