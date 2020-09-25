
# from scipy.optimize import newton
from scipy.optimize import newton as nt

def my_function(x):
    return (x**2 + 2*x + 1)


if __name__ == "__main__":
    print("enter main function")

    # print(newton(my_function, 0))
    print(nt(my_function, 0))
