import numpy as np

# задача 31
# old_settings = np.seterr(divide='ignore')
# print(old_settings)
# print(np.geterr())
# print(123/0)

# задача 32
# print(np.emath.sqrt(-1))
# print(np.sqrt(-1))
# print(np.datetime64('tomorrow'))

# задача 34
# Z = np.arange(input(),input(),dtype='datetime64[D]')

# задача 37.1
# n, m = map(int, input().split())
# k = int(input())
# Z = np.zeros((n,m))+np.arange(k,k+m)

# задача 37.2
# n, m = map(int, input().split())
# k = int(input())
# a = np.array(np.arange(k,k+n))
# Z = np.zeros((n,m)) + np.reshape(a,(-1,1))
# print(Z)

# задача 38
# V = range(10)
# V = map(np.sin, range(10))
# V = {1:2, 3:4}
# Z = np.fromiter(V,float)
# print(Z)

# задача 39.1 (деление отрезка на N+1 часть)
# start, stop, n = [int(input()) for _ in range(3)]
# Z = np.around(np.linspace(start+stop/(n+1), stop, n, False), 3)
# print(Z)

# задача 39.2
# start, stop, n = [int(input()) for _ in range(3)]
# Z = np.around(np.geomspace(start, stop, n), 3)
# print(Z)

# задача 40
seed, n = [int(input()) for _ in range(2)]
np.random.seed(seed)

Z = np.sort(np.random.random(n))
print(Z)
Z = np.sort(np.random.default_rng().uniform(size=n))
print(Z)
Z = np.random.uniform(size=n)
print(Z)


















