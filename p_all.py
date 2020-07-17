
import random

hist = [0] * 7
for i in range(10000):
    dice = random.randint(1, 6)
    hist[dice] += 1

p = [0] * 7
for i in range(1, 7):
    p[i] = hist[i] /10000
    print("show p value: ", p[i])

# print("all p value: ", sum(p))
print("all p value: ", str(sum(p)))
