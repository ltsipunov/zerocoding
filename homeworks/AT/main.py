def add(a, b):
   return a + b

def subtract(a, b):
   return a - b

def multiply(a, b):
   return a * b

def divide(a, b):
    if b==0: raise ValueError('На ноль делить нельзя')
    return a / b

def mod(a, b):
    if b==0: raise ValueError('Н')
    return a % b
