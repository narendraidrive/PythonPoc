import random

def roll_dice():
    print("rolling...")
    return random.randint(1, 6)

def random_sum():
    a = random.randint(1, 10)
    b = random.randint(1, 7)
    return a + b