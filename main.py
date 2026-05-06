import random

streak = 0
coins = 0

while True:
    num = random.randint(1, 10)
    inp = input(f"Choose a number from 1 to 10! Coins: {coins}" + (f", streak: {streak}\n" if streak > 0 else "\n"))
    if inp == str(num):
        print("Correct!")
        streak += 1
        coins += (10 * (1 + (streak / 10)))
    else:
        print("Wrong!")
        streak = 0