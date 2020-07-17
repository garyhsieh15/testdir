
import numpy as np
import matplotlib.pyplot as plt


p = np.matrix([[1, 3, 3, 1], [1, 1, 2, 1], [1, 1, 1, 1]])

s = 2
t = 3
A = np.matrix([[1, 0, s], [0, 1, t], [0, 0 , 1]])
th = np.radians(90)

B = np.matrix([[np.cos(th), np.sin(-th), 0], [np.sin(th), np.cos(th), 0],
    [0, 0, 1]])

# p2 = B * A * p
p2 = A * B * p
print(p2)

p = np.array(p)
p2 = np.array(p2)

plt.plot(p[0, :], p[1, :])
plt.plot(p2[0, :], p2[1, :])
plt.axis('equal')
plt.grid(color = '0.8')
plt.show()
