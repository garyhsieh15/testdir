
import matplotlib.pyplot as plt
import random
import math

def circle():
    cnt = 0
    for i in range(3000):
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        d = math.sqrt((x - 50)**2 + (y - 50)**2)

        if (d <= 50):
            cnt += 1
            plt.scatter(x, y, marker='.', c='r')
        else:
            plt.scatter(x, y, marker='.', c='g')

    plt.axis('equal')
    plt.show()

    p = cnt / 3000
    pi = p * 4
    print("show the pi value: ", pi)
