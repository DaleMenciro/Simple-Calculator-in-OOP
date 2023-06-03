'''
This file inherits from the Operation class 
from operations_calculator.py file

This file adds additional operation methods
such as: square, cube, square root, cube root,
power, and sin.

'''

import math

class AdditionalOperation:
    def __init__(self) -> None:
        pass

    def square(self, number):
        return number ** 2
    
    def cube(self, number):
        return number ** 3
        
    def square_root(self, number):
        return math.sqrt(number)
        
    def cube_root(self,number):
        return math.cbrt(number)
        
    def power(self, base, exponent):
        return math.pow(base,exponent)
        
    def sin(self, angle):
        return math.sin(math.radians(angle))
