import random

def get_random_python_code(max_length=10):
    code = ""
    for i in range(random.randint(1, max_length)):
        code += chr(random.randint(97, 122))
    return code
