import random
from random import sample
total_weight = 713
weights = sorted([random.randint(1, total_weight - 2) for _ in range(2)])
a = weights[0]
b = weights[1] - weights[0]
c = total_weight - weights[1]
weight = [a, b, c]
positions = sample(range(1, 8), 3)
print("There are 3 boxes between 1 and 7 kilometers. You have to find all 3 boxes, and their total weight must be 713kg.")
found_weights = []
while True:
    found_weights.clear()
    guesses = []

    for _ in range(3):
        guess = int(input("Enter distance:"))
        guesses.append(guess)
    
    for guess in guesses:
        if guess in positions:
            found_weights.append(weights[positions.index(guess)])

    if sum(found_weights) == total_weight and len(found_weights) == 3:
        print("\nCongratulations! You found all the cargo!")
        print("Box weights:", found_weights)
        break
    else:
        print("\nWrong guesses! The boxes are moving to new locations...")
        positions = random.sample(range(1, 8), 3)
