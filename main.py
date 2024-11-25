import random
from random import sample

total_weight = 713
box1 = random.randint(1, total_weight)
box2 = random.randint(1, total_weight - box1)
box3 = total_weight - box1 - box2
found_weights = [box1, box2, box3]

positions = sample(range(1, 8), 3)
print("There are 3 boxes between 1 and 7 kilometers. You have to find all 3 boxes, and their total weight must be 713kg.")

while True:
    guesses = []
    
    for _ in range(3):
        guess = int(input("Enter kilometer mark: "))
        guesses.append(guess)

    if sorted(guesses) == sorted(positions):
        print("\nCongratulations! You found all the cargo!")
        print("Box weights:", found_weights)
        break
    else:
        print("\nWrong guesses! The boxes are moving to new locations...")
        positions = random.sample(range(1, 8), 3)
