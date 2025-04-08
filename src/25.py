def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def square_root(x):
    if x < 0:
        raise ValueError("Square root not defined for negative numbers")
    return x ** 0.5
