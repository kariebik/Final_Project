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
button_sin = Button(window, text='sin', padx=40, pady=20, command= lambda: SCT('sin'))
button_cos = Button(window, text='cos', padx=40, pady=20, command= lambda: SCT('cos'))
button_tan = Button(window, text='tan', padx=40, pady=20, command= lambda: SCT('tan'))
button_isin = Button(window, text='sin^-1', padx=40, pady=20, command= lambda: ISCT('sin^-1 '))
button_icos = Button(window, text='cos^-1', padx=40, pady=20, command= lambda: ISCT('cos^-1 '))
button_itan = Button(window, text='tan^-1', padx=40, pady=20, command= lambda: ISCT('tan^-1 '))
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

def SCT(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + num)
    global symbol
    symbol = "sct"

def ISCT(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + num)
    global symbol
    symbol = "isct"

def equals_button():
    """
    This is the command for the equals button. Its action changes depending on the value of symbol to know how to react to the previous button.
    :return:
    """
    if symbol == "+":
        second_number = eval(e.get())
        e.delete(0, END)
        e.insert(0, str(f_num + second_number))
    elif symbol == "sqrt":
        num = e.get()
        second_number = math.sqrt(int(num[1:]))
        e.delete(0, END)
        e.insert(0, str(second_number))
    elif symbol == "()":
        log = e.get()
        b1 = log.find("(")
        b2 = log.find(")")
        base = int(log[3: b1])
        num = eval(log[b1+1:b2])
        e.delete(0, END)
        e.insert(0, str(math.log(num, base)))
    elif symbol == "sct":
        main()
    elif symbol == "curt":
        num = e.get()
        second_number = math.cbrt(int(num[2:]))
        e.delete(0, END)
        e.insert(0, str(second_number))
    elif symbol == "^":
        text = e.get()
        b1 = text.find("^")
        base = int(text[3: b1])
        pwr = eval(text[b1+1:])
        e.delete(0, END)
        e.insert(0, str(base ** pwr))
    elif symbol == "!":
        text =e.get()
        b1 = text.find("!")
        num = eval(text[0:b1])
        e.delete(0, END)
        e.insert(0, str(math.factorial(num)))



def sqrt_button(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + num)
    global symbol
    symbol = "sqrt"

def curt_button(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + num)
    global symbol
    symbol = "curt"

button_sqrt = Button(window, text='√', padx=40, pady=20, command= lambda: sqrt_button("√"))
button_crt = Button(window, text='3√', padx=40, pady=20, command= lambda: curt_button("3√"))
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
    button_sqrt.grid_remove()
    button_log.grid_remove()
    button_sin.grid_remove()
    button_cos.grid_remove()
    button_tan.grid_remove()
    button_x2.grid_remove()
    button_x3.grid(row=3, column=4)
    button_isin.grid(row=1, column=3)
    button_icos.grid(row=2, column=3)
    button_itan.grid(row=3, column=3)
    logx_button.grid(row=4, column=4)
    button_e.grid(row=1, column=4)
    button_crt.grid(row=1, column=5)
    shift.grid_remove()
    shift2.grid(row=2, column=4)


def switch_button2():
    button_e.grid_remove()
    button_x3.grid_remove()
    logx_button.grid_remove()
    button_isin.grid_remove()
    button_icos.grid_remove()
    button_itan.grid_remove()
    button_x2.grid(row=3, column=4)
    button_log.grid(row=4, column=4)
    button_sin.grid(row=1, column=3)
    button_cos.grid(row=2, column=3)
    button_tan.grid(row=3, column=3)
    button_pi.grid(row=1, column=4)
    button_sqrt.grid(row=1, column=5)
    shift2.grid_remove()
    shift.grid(row=2, column=4)

shift = Button(window, text= 'shift', padx=40, pady=20, command= switch_button)
shift2 = Button(window, text= 'shift', padx=40, pady=20, command= switch_button2)

shift.grid(row=2, column=4)
def main():
    global result
    text = e.get()
    operation = text[0:3]
    angle = int(text[3:])
    if operation == "sin":
        result = math.sin(angle)
    elif operation == "cos":
        result = math.cos(angle)
    elif operation == "tan":
        result = math.tan(angle)
    e.delete(0, END)
    e.insert(0, str(result))

def imain():
    global result
    text = e.get()
    operation = text[0:7]
    angle = int(text[7:])
    if operation == "sin^-1 ":
        result = math.asin(angle)
    elif operation == "cos^-1 ":
        result = math.acos(angle)
    elif operation == "tan^-1 ":
        result = math.atan(angle)
    e.delete(0, END)
    e.insert(0, str(result))

def brackets(NUM):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + NUM)
    global symbol
    symbol = "()"
eq_button = Button(window, text='=', padx=100, pady=20, command= equals_button)
eq_button.grid(row=5, column=1, columnspan=2)
open_bracket_button = Button(window, text='(', padx=40, pady=20, command= lambda: brackets("("))
open_bracket_button.grid(row=5, column=3)
close_bracket_button = Button(window, text=')', padx=40, pady=20, command= lambda: brackets(")"))
close_bracket_button.grid(row=5, column=4)

logx_button = Button(window, text='logx', padx=40, pady=20, command= lambda: brackets("log"))

def log_button():
    global f_num
    f_num = eval(e.get())
    result = math.log10(f_num)
    e.delete(0, END)
    e.insert(0, str(result))

button_log = Button(window, text='log', padx=40, pady=20, command=log_button)
button_log.grid(row=4, column=4)

'''
This part of the code creates a log button. The user inputs a number first and than presses the button, and
the computer outputs the answer(The power of 10 such that 10^x = the number given by the user)
Using the shift button the user gets access to logx button. After pressing it, the user will enter the base
and the other number in the logarithm in brackets (logx(y)), and the computer will calculate the value
(The power of the base number such that (base number)^x=y 
'''

def power(NUM):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + NUM)
    global symbol
    symbol = "^"

def factorial_button(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + num)
    global symbol
    symbol = "!"

button_factorial = Button(window, text="!", padx=40, pady=20, command=lambda: factorial_button("!"))
button_factorial.grid(row=4, column=3)

button_x2 = Button(window, text='x^2', padx=40, pady=20, command=lambda: power("^2"))
button_x3 = Button(window, text='x^3', padx=40, pady=20, command=lambda: power("^3"))
button_x2.grid(row=3, column=4)

'''
These lines of the code create a factorial button. Computer reads all the numbers before the "!" sign,
and outputs the factorial value of a given number
'''

def solve_cubic(a, b, c, d):
    p = (3*a*c - b**2) / (3*a**2)
    q = (2*b**3 - 9*a*b*c + 27*a**2*d) / (27*a**3)
    delta = (q/2)**2 + (p/3)**3
    sqrt_delta = (-1)**0.5 * delta
    u1 = (q/2 + sqrt_delta)**(1/3)
    u2 = (q/2 - sqrt_delta)**(1/3)
    y1 = u1 + u2 - b / (3*a)
    y2 = -(u1 + u2) / 2 - b / (3*a) + (u1 - u2) * (3**0.5) / 2j
    y3 = -(u1 + u2) / 2 - b / (3*a) - (u1 - u2) * (3**0.5) / 2j
    return y1, y2, y3
'''
This is the code for solving a cubic equation
'''

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root,
    else:
        return "No Roots"
'''
This piece of code solves a quadratic equation
'''

def eqn_button():
    window_eqn = Tk()
    window_eqn.title("Equation Solver")

    lbl_instruction = Label(window_eqn, text="Choose the type of equation:")
    lbl_instruction.grid(row=1, column=0, columnspan=2, pady=5)

    btn_quadratic = Button(window_eqn, text="Quadratic", command=solve_quadratic_window)
    btn_quadratic.grid(row=1, column=0, padx=5, pady=5)

    btn_cubic = Button(window_eqn, text="Cubic", command=solve_cubic_window)
    btn_cubic.grid(row=1, column=1, padx=5, pady=5)
    '''
    These lines of code create an eqn button. After user presses it a separate window with two buttons will appear
    '''

def solve_quadratic_window():
    window_quadratic = Tk()
    window_quadratic.title("Quadratic Solver")

    lbl_a = Label(window_quadratic, text="Enter coefficient a:")
    lbl_a.grid(row=0, column=0)
    entry_a = Entry(window_quadratic, width=10)
    entry_a.grid(row=0, column=1, padx=5, pady=5)

    lbl_b = Label(window_quadratic, text="Enter coefficient b:")
    lbl_b.grid(row=1, column=0)
    entry_b = Entry(window_quadratic, width=10)
    entry_b.grid(row=1, column=1, padx=5, pady=5)

    lbl_c = Label(window_quadratic, text="Enter coefficient c:")
    lbl_c.grid(row=2, column=0)
    entry_c = Entry(window_quadratic, width=10)
    entry_c.grid(row=2, column=1, padx=5, pady=5)
    '''
    This piece of code creates a separate window for a quadratic equation. After pressing "quadratic" the user
    will be asked to input a, b and c constants
    '''

    def calculate_quadratic():
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        roots = solve_quadratic(a, b, c)
        result_label.config(text=f"Roots: {roots}")

    btn_calculate = Button(window_quadratic, text="Calculate", command=calculate_quadratic)
    btn_calculate.grid(row=3, column=0, columnspan=2, pady=5)

    result_label = Label(window_quadratic, text="")
    result_label.grid(row=4, column=0, columnspan=2, pady=5)
'''
After the user inputs the constants, they will get roots as an output
'''
def solve_cubic_window():
    window_cubic = Tk()
    window_cubic.title("Cubic Solver")

    lbl_a = Label(window_cubic, text="Enter coefficient a:")
    lbl_a.grid(row=0, column=0)
    entry_a = Entry(window_cubic, width=10)
    entry_a.grid(row=0, column=1, padx=5, pady=5)

    lbl_b = Label(window_cubic, text="Enter coefficient b:")
    lbl_b.grid(row=1, column=0)
    entry_b = Entry(window_cubic, width=10)
    entry_b.grid(row=1, column=1, padx=5, pady=5)

    lbl_c = Label(window_cubic, text="Enter coefficient c:")
    lbl_c.grid(row=2, column=0)
    entry_c = Entry(window_cubic, width=10)
    entry_c.grid(row=2, column=1, padx=5, pady=5)

    lbl_d = Label(window_cubic, text="Enter coefficient d:")
    lbl_d.grid(row=3, column=0)
    entry_d = Entry(window_cubic, width=10)
    entry_d.grid(row=3, column=1, padx=5, pady=5)

    '''
    These lines of the code create a separate window for solving a cubic equation. After user presses "cubic"
    they will be asked to input a, b, c and d constants 
    '''

    def calculate_cubic():
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        d = float(entry_d.get())
        roots = solve_cubic(a, b, c, d)
        result_label.config(text=f"Roots: {roots}")

    btn_calculate = Button(window_cubic, text="Calculate", command=calculate_cubic)
    btn_calculate.grid(row=4, column=0, columnspan=2, pady=5)

    result_label = Label(window_cubic, text="")
    result_label.grid(row=5, column=0, columnspan=2, pady=5)
eqn_button = Button(window, text='eqn', padx=40, pady=20, command=eqn_button)
eqn_button.grid(row=5, column=3)
'''
After the user inputs the constants, they will get roots as an output
'''

window.mainloop()
