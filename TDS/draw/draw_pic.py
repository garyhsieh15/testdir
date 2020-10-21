
import numpy as np

# numpy is a module, random is class, rd is member of function
from numpy import random as rd
#from numpy import random
#from matplotlib import pyplot as plt
import matplotlib.pyplot as plt

#import calc_newton
#from .calc_newton import draw_x2_func_curve


def draw_scatter():
    rd.seed(0)
    #rd.seed(10)
    #print("rd.seed(0):", rd.seed(10))
    x = rd.randn(20)
    #print("rd.randn(30):", x)

    y = np.sin(x) + x
    #print("y:", y)
    #print("sin(3.14):", np.sin(3.1415926))
    #print("sin(3.14/2):", np.sin(3.1415926/2))
    
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, "o")

    plt.title("gary hsieh")
    plt.xlabel("XX")
    plt.ylabel("YY")

    #plt.scatter(x, y)
    plt.grid(True)

    plt.show()
    
def draw_continue_curve(_data_account):
    np.random.seed(0)
    numpy_data_x = np.arange(_data_account)
    print("numpy data x:", numpy_data_x)

    numpy_random_data_y = np.random.randn(_data_account).cumsum()
    #print("numpy random data y:", np.random.randn(10))
    #print("numpy random data cumsum y:", numpy_random_data_y)
    
    plt.figure(figsize = (20, 6))
    
    # select type of pic and add label
    plt.plot(numpy_data_x, numpy_random_data_y, label = "gg")
    plt.plot(numpy_data_x * 1.6, numpy_random_data_y * 1.6, label = "ff")
    
    #plt.scatter(numpy_data_x, numpy_random_data_y)

    #plt.plot(numpy_data_x, numpy_random_data_y)
    plt.legend()

    plt.xlabel("X")
    plt.ylabel("Y")

    plt.grid(True)
    plt.show()

def split_pic():
    plt.figure(figsize = (20, 6))

    plt.subplot(2, 1, 1)
    x = np.linspace(-10, 10, 1000)
    print("x value:", x)
    plt.plot(x, np.sin(x), label = "data x")
    plt.legend()

    plt.grid(True)

    plt.subplot(2, 1, 2)
    x1 = np.linspace(-10, 10, 1000)
    print("x1 value:", x1)
    plt.plot(x1, np.sin(3 * x1), label = "data x1")
    plt.legend()

    plt.grid(True)

    plt.show()

def draw_x2_func_curve():
    x = np.arange(-10, 10)
    plt.figure(figsize = (20, 6))
    plt.plot(x, calc_newton.x2_function(x))
    plt.grid(True)

    plt.show()

def draw_hist(_data, _num, _range):
    #rd.seed(0)
    random.seed(0)

    #print("show _range:", _range)
    plt.figure(figsize = (20, 6))
    #plt.hist(rd.randn(10 ** 5) * 10 + 50, bins = 60, range = (20, 80))
    plt.hist(_data, bins = _num, range = _range)

    plt.grid(True)
    plt.show()

def draw_xxfunc():
    x = np.arange(-10, 10)
    plt.figure(figsize = (20, 6))

    plt.plot(x, x ** 2 + 2 * x + 1)
    plt.grid(True)

    plt.show()

if __name__ == "__main__":
    print("enter draw pic main func")
    #draw_scatter()
    #draw_continue_curve()
    #split_pic()

    #data = rd.randn(10 ** 5) * 10 + 50
    """
    data = random.randn(10 ** 5) * 10 + 50
    num = 60
    range = (20, 80)
    draw_hist(data, num, range)
    """
    draw_xxfunc()
