# Random Python Code

import random

def get_random_number(n):
    return random.randint(0, n)

def get_random_number_list(n, m):
    return [get_random_number(m) for _ in range(n)]

# Test the function
print(get_random_number_list(5, 10))
