import random

def math_homework():
    # Generate a random number between 1 and 10
    num = random.randint(1, 10)

    # Ask the user to guess the number
    print("Guess a number between 1 and 10")

    # Loop until the user guesses correctly
    while True:
        guess = int(input())
        if guess == num:
            print("You are correct! The answer is", num)
            break
        elif guess < num:
            print("Too low, try again")
        else:
            print("Too high, try again")

math_homework()