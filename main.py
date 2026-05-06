import random

while True:
    number = random.randint(1, 10)
    inp = input("Choose a number from 1 to 10")
    if inp == str(number):
        print("Correct!")
    else:
        print("Wrong!")