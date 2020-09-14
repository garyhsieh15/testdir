
import numpy as np

a = np.array([2, 4])
b = np.array([3, 1])

cross_ab = np.cross(a, b)

area = np.linalg.norm(cross_ab)

tra_area = area / 2

print("tra area vlaue: ", tra_area)
