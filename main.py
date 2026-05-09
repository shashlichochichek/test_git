import random

streak = 0
coins = 0
best_streak = 0
round_num = 1


def weak_tip(num):
    global coins

    if coins < items["weak_tip"][0]:
        print("Not enough coins!")
        return

    candidates = [x for x in range(1, 11) if x != num]
    coins -= items["weak_tip"][0]
    print(f"The answer is NOT {random.choice(candidates)}")


def normal_tip(num):
    global coins

    if coins < items["normal_tip"][0]:
        print("Not enough coins!")
        return

    candidates = [x for x in range(1, 11) if x != num]
    coins -= items["normal_tip"][0]
    print(f"The answer is NOT any of: {random.sample(candidates, 5)}")


items = {
    "weak_tip":   [3,  weak_tip],
    "normal_tip": [15, normal_tip],
}

num = random.randint(1, 10)

while True:
    shop_hint = " | " + ", ".join(f"{k} ({v[0]}c)" for k, v in items.items())
    inp = input(
        f"\nRound {round_num} | Guess 1-10 | Coins: {coins} | "
        f"Streak: {streak} | Best: {best_streak}"
        f"{shop_hint}\n> "
    ).strip()

    if inp in items:
        items[inp][1](num)
        continue

    if inp == str(num):
        streak += 1
        if streak > best_streak:
            best_streak = streak
        reward = int(10 * (1 + streak / 10))
        coins += reward
        print(f"Correct! +{reward} coins (streak: {streak})")
    else:
        streak = 0
        print(f"Wrong! The number was {num}")

    num = random.randint(1, 10)
    round_num += 1