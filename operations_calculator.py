'''
This file is for the operation methods 
(addition, subtraction, multiplication, and division)
'''

#create class
class Operation:
#create methods for operations
    def add(self, first_number, second_number):
        return first_number + second_number
    
    def subtract(self, first_number, second_number):
        return first_number - second_number

    def multiply(self, first_number, second_number):
        return first_number * second_number
    
    def divide(self, first_number, second_number):
        if second_number == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return first_number / second_number
    
    def calculate(self)