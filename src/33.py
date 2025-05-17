import random

def game_round():
    round_number = random.randint(1, 5)
    if round_number == 1:
        result = "Rock"
    elif round_number == 2:
        result = "Paper"
    elif round_number == 3:
        result = "Scissors"
    else:
        result = "Lizard"

    return result

def main():
    print("Round:", game_round())
