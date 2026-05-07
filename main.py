import random

streak = 0
coins = 0

def weak_tip_fun(num):
    global coins
    rand = random.randint(1, 10)
    if rand == num:
        weak_tip_fun(num)
    else:
        if (coins - items["weak_tip"][0]) < 0:
            print("Not enough coins!")
            return

        print(f"Number is not {rand}!")
        coins -= items["weak_tip"][0]

items = {
    "weak_tip" : [5, weak_tip_fun]
}

def main(num):
    global streak
    global coins
    inp = input(f"Choose a number from 1 to 10! Coins: {coins}" + (f", streak: {streak}\n" if streak > 0 else "\n"))

    if inp == str(num):
        print("Correct!")
        streak += 1
        coins += (10 * (1 + (streak / 10)))
    elif inp in items:
        items[inp][1](num)
        main(num)
    elif inp != str(num):
        print("Wrong!")
        streak = 0

while True:
    num = random.randint(1, 10)
    main(num)