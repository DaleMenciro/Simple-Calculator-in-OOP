'''
This file is for calling the operation file and creating GUI
(addition, subtraction, multiplication, and division)
'''

import tkinter as tk
from tkinter import messagebox
from operations_calculator import Operation

class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple App Calculator")
        self.geometry("350x350")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)

        self.calculator = Operation()

        self.operation_var = tk.StringVar(value="Addition")
        self.create_widgets()

    def create_widgets(self):
        self.operation_label = tk.Label(self, text="Select operation:")
        self.operation_label.grid(row=0, column=0)

        self.addition_radio = tk.Radiobutton(self, text="Addition", variable=self.operation_var, value="Addition")
        self.addition_radio.grid(row=1, column=0)

        self.subtraction_radio = tk.Radiobutton(self, text="Subtraction", variable=self.operation_var, value="Subtraction")
        self.subtraction_radio.grid(row=2, column=0)

        self.multiplication_radio = tk.Radiobutton(self, text="Multiplication", variable=self.operation_var, value="Multiplication") 
        self.multiplication_radio.grid(row=3, column=0)

        self.division_radio = tk.Radiobutton(self, text="Division", variable=self.operation_var, value="Division")
        self.division_radio.grid(row=4, column=0)

    
    #def calculate(self):

app = CalculatorApp()
app.mainloop()