import random
from random import sample
total_weight = 713
weights = sorted([random.randint(1, total_weight - 2) for _ in range(2)])
a = weights[0]
b = weights[1] - weights[0]
c = total_weight - weights[1]
weight = [a, b, c]
list = [1, 2, 3, 4, 5, 6, 7]
positions = sample(list, 3)
print("There are 3 boxes between 1 and 7 kilometers. You have to find all 3 boxes, and their total weight must be 713kg.")
while True:
    guesses = []

    for _ in range(3):
        guess = int(input("Enter distance:"))
        guesses.append(guess)
    for guess in guesses:
        if guess in positions:
            weight = weights[positions.index(guess)]
