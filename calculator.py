class Calculator:

    def add(self, a, b):
        return a+b
    
    def subtract(self, a, b):
        return a-b
    
    def multiply(self, a, b):
        return a*b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError('Can not divide by 0')
        return a / b
    
