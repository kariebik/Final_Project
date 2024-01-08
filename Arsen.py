import tkinter as tk
import math

class ScientificCalculator(tk.Tk):
    def init(self):
        # Initialize the Tkinter window
        super().init()
        self.title("Scientific Calculator")
        self.geometry("400x500")

        # Variable to hold the calculation result
        self.result_var = tk.StringVar()

        # Entry widget for displaying the calculation
        entry = tk.Entry(self, textvariable=self.result_var, font=('Arial', 18), bd=10, relief=tk.GROOVE, justify="right")
        entry.grid(row=0, column=0, columnspan=4)

        # Define buttons with their labels and grid positions
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 3, 5),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 4, 5),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 5, 5),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("(", 5, 0), (")", 5, 1), ("Shift", 5, 2), ("AC", 5, 3)
        ]

        # Create buttons and place them on the grid
        for (text, row, col) in buttons:
            button = tk.Button(self, text=text, padx=20, pady=20, font=('Arial', 14), command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=col)

        # Variable to track the state of the Shift key
        self.shift_pressed = False

    def button_click(self, text):
        # Handle button clicks
        if text == "=":
            try:
                # Evaluate the expression and display the result
                expression = self.result_var.get()
                if self.shift_pressed:
                    # Use a restricted set of functions when Shift is pressed
                    result = eval(expression, {"builtins": None}, {'sqrt': math.sqrt, 'sin': math.sin, 'cos': math.cos, 'tan': math.tan})
                else:
                    # Evaluate the expression using eval()
                    result = eval(expression)
                self.result_var.set(result)
            except Exception as e:
                # Handle errors by displaying "Error"
                self.result_var.set("Error")
        elif text == "AC":
            # Clear the entire calculation
            self.result_var.set("")
        elif text == "Shift":
            # Toggle the state of the Shift key
            self.shift_pressed = not self.shift_pressed
        else:
            # Handle other button clicks
            current_text = self.result_var.get()
            if text == "(" and current_text and current_text[-1].isdigit():
                # Auto-insert "*" before an opening parenthesis when a digit precedes it
                self.result_var.set(current_text + "*(")
            elif text == ")" and current_text and current_text[-1] == "(":
                # Auto-insert "1" after an opening parenthesis
                self.result_var.set(current_text + "1)")
            else:
                # Append the clicked button's text to the current calculation
                self.result_var.set(current_text + text)

if __name__ == "main":
    # Create an instance of the ScientificCalculator class and start the main loop
    calculator = ScientificCalculator()
    calculator.mainloop()