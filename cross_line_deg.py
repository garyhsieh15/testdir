# ------------------------------------------------
# cal cross line deg
#
#          a1*b1 + a2*b2
# cos =   ---------------
#             |a|*|b|
# ------------------------------------------------

import math
import numpy as np

def cross_line_deg():
    # input array value:
    a = np.array([2, 7])
    b = np.array([6, 1])
    c = np.array([2, 3])
    d = np.array([6, 5])

    # cal vector a and b
    va = b - a
    vb = d - c

    # abs |vector| 
    norm_a = np.linalg.norm(va)
    norm_b = np.linalg.norm(vb)

    # dot product
    dot_ab = np.dot(va, vb)

    #cal rad and deg
    cos_th = dot_ab / (norm_a * norm_b)
    rad = math.acos(cos_th)
    deg = math.degrees(rad)

    print("deg value: ", deg)

if __name__ == "__main__":
    cross_line_deg()
