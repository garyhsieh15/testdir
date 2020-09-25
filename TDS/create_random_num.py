
import numpy as np
import numpy.random as random

N = 10 ** 2

normal_data = [random.random for _ in range(N)]
#normal_data = [random.random for a in range(N)]

for i in range(N):
    print("show normal data for method 1:", normal_data[i])
"""
normal_data = [0] * N
for i in range(N):
    #print("show random value:", random.random)
    print("show start normal_data[",i,"]:",normal_data[i])
    #normal_data[i] = random.random
    #print("show after normal_data[i]:", normal_data[i])
    normal_data[i] = random.random
    #print("show i value:", i)
    print("show after normal_data[",i,"]:", normal_data[i])
"""
"""
print("show normal data out:", normal_data)
#print("show random number data len:", len(normal_data))
#print("show random number data:", random_num_data)
"""
random_num_data = np.array(normal_data)
#print("show random number data:", random_num_data)
#print("show [0] value:", random_num_data[0])
#print("show [1] value:", random_num_data[1])
