
import itertools

num = {1, 2, 3, 4, 5}
A = set(itertools.permutations(num, 2))

A_len = len(A)
print("A lenghts: ", A_len)

for i in A:
    print("result:", i)
