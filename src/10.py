import random

def get_random_math_problem(difficulty):
    if difficulty == "easy":
        operation = ["+", "-"]
    elif difficulty == "medium":
        operation = ["+", "-", "*", "/"]
    else:
        operation = ["+", "-", "*", "/", "%"]
    
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    op = random.choice(operation)
    
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    else:
        result = num1 / num2
        
    return "What is {} {} {}?".format(num1, op, num2)