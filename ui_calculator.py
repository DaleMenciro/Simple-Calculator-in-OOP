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
