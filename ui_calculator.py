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
    
        self.num1_label = tk.Label(self, text="Enter first number:")
        self.num1_label.grid(row=0, column=1)

        self.num1_entry = tk.Entry(self)
        self.num1_entry.grid(row=1, column=1)

        self.num2_label = tk.Label(self, text="Enter second number:")
        self.num2_label.grid(row=2, column=1)

        self.num2_entry = tk.Entry(self)
        self.num2_entry.grid(row=3, column=1)

        #Calculate, Result, Clear, Try Again, and Exit button
        self.calculate_button = tk.Button(self, text="Calculate", command=self)
        self.calculate_button.grid(row=4, column=1, sticky="NSEW")

        self.result_label = tk.Label(self, text="Result:")
        self.result_label.grid(row=5, column=1, sticky="NSEW")

        self.clear_button = tk.Button(self, text="Clear", command=self)
        self.clear_button.grid(row=6, column=0, sticky="NSEW")

        self.try_again_button = tk.Button(self, text="Try Again", command=self)
        self.try_again_button.grid(row=6, column=1, sticky="NSEW")

        self.exit_button = tk.Button(self, text="Exit", command=self)
        self.exit_button.grid(row=6, column=2, sticky="NSEW")

    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())

            operation = self.operation_var.get()
    
    def clear(self):
        self.num1_entry.delete(0,tk.END)
        self.num2_entry.delete(0, tk.END)
        self.result_label.config(text="Result: ")
    def try_again(self):
    
    def exit_program(self):
app = CalculatorApp()
app.mainloop()