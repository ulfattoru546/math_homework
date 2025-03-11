
import random
def generate_random_number(n):
    if n < 1:
        raise ValueError("n must be at least 1")
    numbers = []
    for i in range(n):
        numbers.append(random.randint(1, n))
    return numbers