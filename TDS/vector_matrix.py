
import numpy as np
#from numpy import random
from numpy import random as rd

def create_random():
    print("enter create_random() funciton")
    #random.seed(0)

    #aa = random.randn(10)
    aa = rd.randn(10)
    print("show aa value:", aa)

def show_info():
    data = np.array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    data1 = np.array([1, 2, 3, 4])

    print("show vector data's data type:", data.dtype)
    print("show vector data1's data type:", data1.dtype)
    print("show data[0]:", data[0])
    print("show data1[1]:", data1[1])
    print("show ndim:", data.ndim)
    print("show size:", data.size)

    print("show data sort:", data.sort())
    print("show data again:", data)
    print("show data big to small:", data[::-1])
    print("show data again:", data)
    print("show data sort:", data.sort())
    print("show data[::-1]:", data[::-1].sort())
    print("show data again:", data)

if __name__ == "__main__":
    show_info()
