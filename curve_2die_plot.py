
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-100.0, 100.01, 0.01)
# y = 10 * x
y = x**2

plt.plot(x, y)
plt.grid(color = '0.8')
plt.show()
