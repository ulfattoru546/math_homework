def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Divisor cannot be zero."

print(add(10, 20))
print(subtract(10, 5))
print(multiply(10, 20))
print(divide(10, 3))
