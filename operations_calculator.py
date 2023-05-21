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
    
    def calculate(self, operation, first_number, second_number)
        try:
            if operation == "Addition":
                return self.add(first_number, second_number)
            elif operation == "Subtraction":
                return self.subtract(first_number, second_number)
            elif operation == "Multiplication":
                return self.multiply(first_number, second_number)
            elif operation == "Division":
                return self.divide(first_number, second_number)