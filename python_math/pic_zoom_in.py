
import numpy as np
import matplotlib.pyplot as plt

p = np.matrix([[1, 1, 2, 1], [3, 1, 1, 3]])

A = np.matrix([[3, 0], [0, 3]])
# A = 20 * np.matrix([[3, 0], [0, 3]])

p2 = A * p
print("p2 value: ", p2)

p = np.array(p)
p2 = np.array(p2)

plt.plot(p[0, :], p[1, :])
plt.plot(p2[0, :], p2[1, :])
plt.axis('equal')

plt.grid(color = '0.8')
plt.show()

