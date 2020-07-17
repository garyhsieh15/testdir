# -----------------------------------------------
# cal area via Heron's formula
# s = (a + b + c) / 2
# S = sqrt(s(s-a)(s-b)(s-c))
#
# ----------------------------------------------- 
import math

x = [1, 3, 6]
y = [5, 1, 4]

a = math.sqrt((x[1] - x[0])**2 + (y[1] - y[0])**2)
b = math.sqrt((x[2] - x[1])**2 + (y[2] - y[1])**2)
c = math.sqrt((x[2] - x[0])**2 + (y[2] - y[0])**2)

s = (a + b + c)/2

print("area:", math.sqrt(s*(s - a)*(s - b)*(s - c)))

# print("area: ", area)

