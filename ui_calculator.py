'''
This file is for calling the operation file and creating GUI
(addition, subtraction, multiplication, and division)

With inheritance, the methods within AdditionalOperation class will be added to the program.
(Square, Cube, Square Root, and Cube Root)
Only the number on firs number will be calculated if the user prompt the said operations.
'''

import tkinter as tk
from tkinter import messagebox
from operations_calculator import Operation
from additional_operations_calculator import AdditionalOperation

class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple App Calculator")
        self.geometry("450x450")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=1)
        self.rowconfigure(8, weight=1)
        self.rowconfigure(9, weight=1)

        self.calculator = Operation()
        self.additional_operations = AdditionalOperation()

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

        self.square_button = tk.Radiobutton(self, text="Square", variable=self.operation_var, value="Square")
        self.square_button.grid(row=5, column=0)

        self.cube_button = tk.Radiobutton(self, text="Cube", variable=self.operation_var, value="Cube")
        self.cube_button.grid(row=6, column=0)

        self.square_root_button = tk.Radiobutton(self, text="Square Root", variable=self.operation_var, value="Square Root")
        self.square_root_button.grid(row=7, column=0)

        self.cube_root_button = tk.Radiobutton(self, text="Cube Root", variable=self.operation_var, value="Cube Root")
        self.cube_root_button.grid(row=8, column=0)
    
        self.num1_label = tk.Label(self, text="Enter first number:")
        self.num1_label.grid(row=0, column=1)

        self.num1_entry = tk.Entry(self)
        self.num1_entry.grid(row=1, column=1)

        self.num2_label = tk.Label(self, text="Enter second number:")
        self.num2_label.grid(row=2, column=1)

        self.num2_entry = tk.Entry(self)
        self.num2_entry.grid(row=3, column=1)

        #Calculate, Result, Clear, Try Again, and Exit button
        self.calculate_button = tk.Button(self, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=4, column=1, sticky="NSEW")

        self.result_label = tk.Label(self, text="Result:")
        self.result_label.grid(row=5, column=1, sticky="NSEW")

        self.clear_button = tk.Button(self, text="Clear", command=self.clear)
        self.clear_button.grid(row=9, column=0, sticky="NSEW")

        self.try_again_button = tk.Button(self, text="Try Again", command=self.try_again)
        self.try_again_button.grid(row=9, column=1, sticky="NSEW")

        self.exit_button = tk.Button(self, text="Exit", command=self.exit_program)
        self.exit_button.grid(row=9, column=2, sticky="NSEW")

    def calculate(self):
        operation = self.operation_var.get()
        num1 = float(self.num1_entry.get())

        if operation in ["Square", "Cube", "Square Root", "Cube Root"]:
            self.calculate_first_number(operation, num1)
        else:
            try:
                num2 = float(self.num2_entry.get())

                if operation == "Addition":
                    result = self.calculator.add(num1, num2)
                elif operation == "Subtraction":
                    result = self.calculator.subtract(num1, num2)
                elif operation == "Multiplication":
                    result = self.calculator.multiply(num1, num2)
                elif operation == "Division":
                    result = self.calculator.divide(num1, num2)
                
                self.result_label.config(text=f"Result: {result: .2f}")
            except ValueError: 
                messagebox.showerror("Error", "Invalid input! Please enter a valid number.")
            except ZeroDivisionError as e:
                messagebox.showerror("Error", e)               

    def calculate_first_number (self, operation, num1):
            if operation == "Square":
                result = self.additional_operations.square(num1)
            elif operation == "Cube":
                result = self.additional_operations.cube(num1)
            elif operation == "Square Root":
                result = self.additional_operations.square_root(num1)
            elif operation == "Cube Root":
                result = self.additional_operations.cube_root(num1)

            self.result_label.config(text=f"Result: {result: .2f}")


    def clear(self):
        self.num1_entry.delete(0,tk.END)
        self.num2_entry.delete(0, tk.END)
        self.result_label.config(text="Result: ")

    def try_again(self):
        self.clear()
        messagebox.showinfo("Try Again", "Please enter new values and Operation")
    
    def exit_program(self):
        self.destroy()
        messagebox.showinfo("Message", "Thank you for using the program!")