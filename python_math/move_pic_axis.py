
import numpy as np
import matplotlib.pyplot as plt

p = np.matrix([[1, 3, 3, 1], [1, 1, 2, 1]])

A = np.matrix([[1, 0], [0, -1]])

p2 = A * p
print("matrix p: ", p)
print("matirx p2: ", p2)

# print("-----------------------------")
# print("p[0, 0]: ", p[0, 0])
# for i in p[0, :]:
#    print("i value: ", i)

p = np.array(p)
p2 = np.array(p2)

# print("------------------------------")
# print("p'[0, 0]: ", p[0, 0])
# print("p'[1, 0]: ", p[1, 0])
# print("p'[1, 2]: ", p[1, 2])
# for i in p[0, :]:
#    print("i' value: ", i)

# print("array p:", p)
# print("array p2:", p2)

plt.plot(p[0, :], p[1, :])
plt.plot(p2[0, :], p2[1, :])

plt.axis('equal')
plt.grid(color = "0.8")

plt.show()
