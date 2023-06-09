'''
This file inherits from the Operation class 
from operations_calculator.py file

This file adds additional operation methods
such as: square, cube, square root, and cube root.

'''

import math
from operations_calculator import Operation

class AdditionalOperation(Operation):
    def __init__(self) -> None:
        super().__init__()

    def square(self, number):
        return number ** 2
    
    def cube(self, number):
        return number ** 3
        
    def square_root(self, number):
        return math.sqrt(number)
        
    def cube_root(self,number):
        return math.pow(number, 1/3)