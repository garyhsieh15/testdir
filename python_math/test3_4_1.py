from sympy import Symbol, solve

print("this is test3_4_1.py")

a = Symbol('a')
b = Symbol('b')
c = Symbol('c')


ex1 = 4*a + 3*b + 3*c - 350
ex2 = 4*a + 2*b + 5*c - 360
ex3 = 8*a + 8*b + 10*c - 840

ans = solve((ex1, ex2, ex3))
print(ans)

print("ex1 value: ", ans[a])
print("ex2 value: ", ans[b])
print("ex3 value: ", ans[c])
