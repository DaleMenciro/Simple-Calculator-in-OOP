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
        