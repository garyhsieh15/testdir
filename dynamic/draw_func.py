
import numpy as np
import math
import matplotlib.pyplot as plt

from sympy import *

# --------------------------------------------------------------------------
# name       : theoretical solution
# description:
#
# data       : 20201209
# author     : garyhsieh
# --------------------------------------------------------------------------
def theo_sol():

    #td_div_Tn = [1/8, 1/4, 1/2, 3/4, 1, 1.5, 2, 2.5, 3, 3.5, 4, 5]
    # jump 1
    td_div_Tn = [2.5]
    time_slice = 100
    for i in td_div_Tn:
        u = []
        ufree = []
        ust = []
        for j in np.arange(0, i + i/time_slice, i/time_slice):
            # j = t/Tn
            # tndt = Tn_div_td
            tndt = 1/i
            pi = 3.1415926
            y = ( 1 / (1 - tndt ** 2) ) * ( math.sin( 2 * pi * j / i ) - tndt * math.sin(2 * pi * j))
            #print("show forced,  i, j, y value:", i, j, y)
            u.append(y)
        for k in np.arange(i, i * 2, i/time_slice):
            yfree = (tndt / (1 - (tndt ** 2))) * ( -math.sin(2 * pi * k) + math.sin(2 * pi * (k - i)) )
            #yfree = (tndt * math.cos(pi * i / 2) / (1 - (tndt ** 2))) * ( -math.sin(2 * pi * (k - i /4 )))
            #print("show free, i, k, yfree value:", i, k, yfree)
            ufree.append(yfree)

        for l in np.arange(0, i * 2, i * 2 / time_slice):
            yst = math.sin( 2 * pi * (1 / i) * l)
            ust.append(yst)
    """
        plt.figure(figsize = (20, 6))
        plt.plot(np.arange(0, i + i/time_slice, i/time_slice), u, label = "forced, td/Tn = " + str(i))
        plt.plot(np.arange(i, i * 2, i/time_slice), ufree, label = "free, td/Tn =" + str(i))
        plt.plot(np.arange(0, i * 2, i * 2 / time_slice), ust, label = "ust, td/Tn =" + str(i))
        plt.grid(True)
        plt.legend()
        plt.xlabel("t/Tn")
        plt.ylabel("u(t)/(ust)0")

    plt.show()
    """
    ux = np.arange(0, i + i/time_slice, i/time_slice)
    ufreex = np.arange(i, i * 2, i/time_slice)
    ustx = np.arange(0, i * 2, i * 2 / time_slice)

    return u, ufree, ust, ux, ufreex, ustx

def all_theo_sol():
    #td_div_Tn = [1/8, 1/4, 1/2, 3/4, 1, 1.5, 2, 2.5, 3, 3.5, 4, 5]
    # jump 1
    td_div_Tn = [1/8, 1/4, 1/2, 3/4, 0.9999, 1.5, 2, 2.5, 3, 3.5, 4, 5]
    time_slice = 100
    for i in td_div_Tn:
        u = []
        ufree = []
        ust = []
        for j in np.arange(0, i + i/time_slice, i/time_slice):
            # j = t/Tn
            # tndt = Tn_div_td
            tndt = 1/i
            pi = 3.1415926
            y = ( 1 / (1 - tndt ** 2) ) * ( math.sin( 2 * pi * j / i ) - tndt * math.sin(2 * pi * j))
            #print("show forced,  i, j, y value:", i, j, y)
            u.append(y)
        for k in np.arange(i, i * 2, i/time_slice):
            yfree = (tndt / (1 - (tndt ** 2))) * ( -math.sin(2 * pi * k) + math.sin(2 * pi * (k - i)) )
            #yfree = (tndt * math.cos(pi * i / 2) / (1 - (tndt ** 2))) * ( -math.sin(2 * pi * (k - i /4 )))
            #print("show free, i, k, yfree value:", i, k, yfree)
            ufree.append(yfree)

        for l in np.arange(0, i * 2, i * 2 / time_slice):
            yst = math.sin( 2 * pi * (1 / i) * l)
            ust.append(yst)

        plt.figure(figsize = (20, 6))
        plt.plot(np.arange(0, i + i/time_slice, i/time_slice), u, label = "forced, td/Tn = " + str(i))
        plt.plot(np.arange(i, i * 2, i/time_slice), ufree, label = "free, td/Tn =" + str(i))
        plt.plot(np.arange(0, i * 2, i * 2 / time_slice), ust, label = "ust, td/Tn =" + str(i))
        plt.grid(True)
        plt.legend()
        plt.xlabel("t/Tn")
        plt.ylabel("u(t)/(ust)0")

    plt.show()


if __name__ == "__main__":
    theo_sol()
    #all_theo_sol()
