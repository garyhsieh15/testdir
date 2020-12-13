
import numpy as np
import math
import matplotlib.pyplot as plt

from sympy import *


def FEM_HW04():
    print("enter FEM_HW04 func")

    u = []
    for x in np.arange(0, 1, 0.01):
        y = -x**3 - 3 * x**2 -3 * x + 3 * math.log(1 + x) + 7.099 * math.log(1 + x) 
        u.append(y)

    plt.figure(figsize = (20, 6))
    plt.plot(np.arange(0, 1, 0.01), u, label = "exact")
    
    x_4linear = [0, 0.25, 0.5, 0.75, 1]
    y_4linear = [0, 1.2996, 1.7194, 1.2921, 0]
    plt.plot(x_4linear, y_4linear, label = "4-linear", linestyle = "--")

    x_2quadratic = [0, 0.25, 0.5, 0.75, 1]
    y_2quadratic = [0, -1.8119, -2.2716, -1.6172, 0]
    plt.plot(x_2quadratic, y_2quadratic, label = "2-quadratic", linestyle = "-.")

    plt.grid(True)
    plt.legend()
    plt.xlabel("axial-dir")
    plt.ylabel("horizontal displacement")

    plt.show()

    print("show math.log(1): ", math.log(1))
    print("show math.log(2.71828): ", math.log(2.71828))

def FEM_HW05_shear(): 
    print("enter FEM_HW05 shear func")
    
    q = 1
    L = 1

    exact_V = []
    for x in np.arange(0, 1.01, 0.01):
        V = (-q/(4 * L**3)) * x**4 + ((q * L)/20) 
        exact_V.append(V)
        print("show x and V: ", x, V)

    plt.figure(figsize = (20, 6))
    plt.plot(np.arange(0, 1.01, 0.01), exact_V, label = "exact V")
     
    x_equilibrium = [0, 0.5, 1]
    y_equilibrium = [1/20, 11/320, -1/5]
    plt.plot(x_equilibrium, y_equilibrium, label = "equilibrium", linestyle = "--")

    x_mathematical = [0, 0.5, 0.5, 1]
    y_mathematical = [67001/1400000, 67001/1400000, -55751/1400000, -55751/1400000]
    plt.plot(x_mathematical, y_mathematical, label = "mathematical", linestyle = "-.")
    
    plt.grid(True)
    plt.legend()
    plt.xlabel("x-dir")
    plt.ylabel("shear force")

    plt.show()

def FEM_HW05_moment():
    print("enter FEM HW05 moment func") 
    q = 1
    L = 1

    exact_M = []
    for x1 in np.arange(0, 1.01, 0.01):
        M = (-q/(20 * L**3)) * x1**5 + ((q * L)/20) * x1
        exact_M.append(M)

    plt.figure(figsize = (20, 6))
    plt.plot(np.arange(0, 1.01, 0.01), exact_M, label = "exact M")
    
    x_equilibrium = [0, 0.5, 1]
    y_equilibrium = [0, 3/128, 0]
    plt.plot(x_equilibrium, y_equilibrium, label = "equilibrium", linestyle = "--")

    x_mathematical = [0, 0.5, 0.5, 1]
    y_mathematical = [2311/8400000, 101656/4200000, 43469/1400000, 31187/2800000]
    plt.plot(x_mathematical, y_mathematical, label = "mathematical", linestyle = "-.")

    plt.grid(True)
    plt.legend()
    plt.xlabel("x-dir")
    plt.ylabel("moment force")

    plt.show()


def D_of_s00():
    print("dynamic of structure")
    #print("show exp(1): ", math.exp(1))
    #print("show sin(3.1415926): ", math.sin(3.1415926))
    
    for damping_ratio in np.arange(0.00, 0.06, 0.01):
        #damping_ratio = 0.05
        damping_ratio_a = ( 1 - damping_ratio ** 2 ) ** 0.5
        u = []
        for x in np.arange(0, 20, 0.01):
            temp = 2 * math.pi * x
            y = ( 1 / damping_ratio_a ) * math.exp( -1 * damping_ratio * temp ) * math.sin( damping_ratio_a * temp )
            u.append(y)
        
        plt.figure(figsize = (20, 6))
        plt.plot(np.arange(0, 20, 0.01), u, label = "damping_ratio = " + str(damping_ratio))
        
        plt.grid(True)
        plt.legend()
        plt.xlabel("t/Tn")
        plt.ylabel("u(t)/(u'(0))/Wn")

    plt.show()

     

if __name__ == "__main__":
    print("enter main function")
    #FEM_HW04()
    #D_of_s00()
    FEM_HW05_shear()
    #FEM_HW05_moment()

