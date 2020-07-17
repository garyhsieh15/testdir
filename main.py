
import matplotlib.pyplot as plt
import numpy as np
import cross_line_deg as cld

def draw_circle():
    r = 300
    x = np.arange(-r, r + 1)
    y = np.sqrt(r**2 - x**2)
    ny = y * -1

    plt.plot(x, y)
    plt.plot(x, ny)
    plt.axis('equal')
    plt.grid(color = '0.8')
    plt.show()

def func00():
    print("call func00 ---->")


if __name__ == "__main__":
    cld.cross_line_deg()
    draw_circle()
