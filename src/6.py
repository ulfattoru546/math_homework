import random

def get_random_math_problem(numbers=None):
    if numbers is None:
        numbers = []
    num1 = random.choice(numbers) if numbers else random.randint(0, 9)
    num2 = random.choice(numbers) if numbers else random.randint(0, 9)
    op = random.choice(['+', '-', '*', '/'])
    answer = eval(str(num1) + op + str(num2))
    return (num1, num2, op, answer)

numbers = [1, 2, 3, 4]
problem = get_random_math_problem(numbers)
print(problem)
