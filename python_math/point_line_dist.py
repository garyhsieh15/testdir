# ==============================================
# cal point and line distance.
#
#               | ax1 + by1 + c |
#              -------------------
#                (a^2 + b^2)^0.5
#
# ===============================================

import matplotlib.pyplot as plt
import math

x = 1
y = 6

a = 3
b = -4
c = -4

result = math.fabs(a * x + b * y + c)/math.sqrt(a**2 + b**2)

print("result: ", result)
