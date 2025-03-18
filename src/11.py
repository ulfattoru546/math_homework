import random

def get_random_math_problem(difficulty):
    numbers = [1, 2, 3, 4, 5]
    operators = ['+', '-', '*', '/']
    
    num1 = random.choice(numbers)
    num2 = random.choice(numbers)
    operator = random.choice(operators)
    
    if difficulty == 'easy':
        answer = eval(str(num1) + operator + str(num2))
    elif difficulty == 'medium':
        answer = eval(str(num1) + operator + str(num2) + '*2')
    else: # difficulty == 'hard'
        answer = eval(str(num1) + operator + str(num2) + '*3')
    
    return num1, num2, operator, answer
