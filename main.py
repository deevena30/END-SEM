from operation import vectorized, nonvectorized
import numpy as np
from matplotlib import pyplot as plt
import time
nonvec = []
vec = []
list = list(range(1,101))
N_square = []
N_cube = []
N_one = []
for i in list:
    matrix = np.random.rand(i,i)
    
    start = time.time()
    nonvectorized(matrix)
    end = time.time()
    nonvec.append(end-start)

    start = time.time()
    vectorized(matrix)
    end = time.time()
    vec.append(end-start)
    
    
for k in list:
    none = k/1e6
    N_one.append(none)
    nsquare = k**2/1e6
    N_square.append(nsquare)
    ncube = k**3/1e6
    N_cube.append(ncube)
    

plt.plot(list, nonvec, label='Non-Vectorized', color='r')
plt.plot(list, vec, label='Vectorized', color='g')
plt.plot(list, N_one,'b--',label='O(N)')
plt.plot(list, N_square,'r--',label='O(N^2)')
plt.plot(list, N_cube,'g--',label='O(N^3)')
plt.show()