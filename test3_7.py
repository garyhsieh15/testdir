import matplotlib.pyplot as plt
import numpy as np

print("this is test3_7.py")

def draw_circle():

    th = np.arange(0, 360)

    x = np.cos(np.radians(th))
    y = np.sin(np.radians(th))

    plt.plot(x, y)
    plt.axis('equal')
    plt.grid(color = '0.8')

    plt.show()
