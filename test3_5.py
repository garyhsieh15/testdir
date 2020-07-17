import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-1, 6)
y = 1/2 * x + 1/2
y2 = -2 * x + 7

print("this is test3_5.py")

plt.plot(x, y)
plt.plot(x, y2)
plt.axis('equal')
plt.grid(color = '0.8')
plt.show()
