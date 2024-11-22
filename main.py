import random
total_weight = 713
weights = sorted([random.randint(1, total_weight - 2) for _ in range(2)])
a = weights[0]
b = weights[1] - weights[0]
c = total_weight - weights[1]
weight = [a, b, c]
