
import numpy as np
import matplotlib.pyplot as plt

p = np.matrix([[0, 0, 1, 1, 0], [1, 0, 0, 1, 1]])

x = np.arange(-1.0, 1.01, 0.01)
y = x

th = np.radians(45)
A = np.matrix([[np.cos(th), np.sin(-th)], [np.sin(th), np.cos(th)]])

p2 = A * p
print("p2 value: ", p2)

# draw picture
p = np.array(p)
p2 = np.array(p2)

plt.plot(x, y)

plt.plot(p[0, :], p[1, :])
plt.plot(p2[0, :], p2[1, :])
plt.axis('equal')
plt.grid(color = '0.8')
plt.show()
