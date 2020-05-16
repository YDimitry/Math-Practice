from functools import reduce
from operator import mul

import numpy as np

# задача 2
# print(np.version.version)


# задача 3.1
# Z = np.array([0]*int(input()))
# print(Z)

# задача 3.2

# s = input().split()
#
# if s[-1].isnumeric():
#     shape = tuple(map(int,s))
#     dtype = float
# else:
#     shape = tuple(map(int,s[:-1]))
#     dtype = s[-1]
#
# Z = np.zeros(shape,dtype)
# print(Z)

# задача 4
# Z = np.zeros((10,10),dtype=np.bool)
# print(reduce(mul, Z.shape+(Z.itemsize,)))

# задача 5
# print(np.info(np.add))
# print(np.add.__doc__)
# print(np.array.__doc__)

# задача 6
# size, n  = map(int, [input() for _ in range(2)])
# Z = np.zeros((size,))
# Z[n] = 1
# print(Z)

# задача 7
# n, m = map(int, [input() for _ in range(2)])
# Z = np.array(np.arange(n,m+1))
# print(Z)

# задача 8
# Z = np.array([1, 2, 3, 4])
# Z = Z[::-1]
# print(Z)

# задача 9
# n = int(input())
# m, i = map(int, input().split())
#
# Z = np.array(np.array_split(np.arange(n),m))
# print(Z)

# задача 10.1
# Z = np.array([1, 0, 2, 0, 3, 0, 4])
# NonZerros = Z[Z > 0]
# NonZerros = np.nonzero(Z)
# print(NonZerros)

# задача 10.2
Z = np.array([[[1, 2],
           [4, 5]],
          [[7, 8],
           [0, 0]]])

print(Z[Z>3].tolist())

# n = np.nan
# m = np.nan
# print(id(n), id(m), sep='\n')
# print(id(n) == id(m))
# print(0* m)









































