
import random

cnt = 0
for i in range(10000):
    dice = random.randint(1, 6)
    if dice == 1:
        cnt += 1

p = cnt / 10000

print("i value: ", i)
print("probility: ", p)
print("1/6 = ", 1/6)

"""
for i in range(10):
    print("(1, 8): ", random.randint(1, 8))
"""
