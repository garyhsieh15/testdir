from sympy import Symbol, solve

print("This is test3_4.py file")

def solve_a_b():
    a = Symbol('a')
    b = Symbol('b')

    ex1 = a + b - 1
    ex2 = 5*a + b - 3

    print(solve((ex1, ex2)))
