import random

streak = 0

while True:
    number = random.randint(1, 10)
    inp = input(f"Choose a number from 1 to 10!" + (f" streak: {streak}\n" if streak > 0 else "\n"))
    if inp == str(number):
        print("Correct!")
        streak += 1
    else:
        print("Wrong!")
        streak = 0