import numpy as np
np.random.seed(42)

# задача 11
# Z = np.eye(int(input()),dtype=int)
# print(Z)

# задача 12
# Z = np.random.random(tuple(map(int, input().split())))
# print(Z)

# задача 13
# Z = np.random.random(tuple(map(int, input().split())))
# print(np.amin(Z))
# print(np.amax(Z))

# задача 14
# Z = np.random.random(tuple(map(int, input().split())))
# print(np.mean(Z))

# задача 15
# Z = np.random.random(tuple(map(int, input().split())))
# Z = np.array([[0.1,0.5,0.8],[0.2,0.6,0.9],[0.1,0.5,0.9],[0.2,0.6,0.9]])
# m = np.mean(Z, axis=0)
# print(np.amin(m))
# print(np.amax(m))

# задача 16
# Z = np.zeros(tuple(map(int, input().split())))
# Z[:,0].fill(1)
# Z[:,-1].fill(1)
# Z[-1,:].fill(1)
# Z[0,:].fill(1)

# задача 17
# Z = np.array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])
#
# Z = np.pad(Z,1,mode='constant', constant_values=1)
# print(Z)

# задача 18.1
# Z = np.diag(np.arange(1,int(input())+1))
# print(Z)

# задача 18.2
# x, k = map(int, input().split())
# Z = np.diag(np.arange(1,k+1),x)
# print(Z)

# задача 19
# n, m = map(int, input().split())
n, m = 3, 5
Z = np.zeros((n,m))
Z[::2,1::2] = 1
Z[1::2,::2] = 1
print(Z)

print()
Z = np.tile([[0.,1.],[1.,0.]],(n, m))[:n,:m]

print(Z)


# задача 20
# i = 5
# Z = np.array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]])
#
# i = 3
# Z = np.array([ 10,  11,  12,  13,  14,  15])
#
# i = 4
# Z = np.array([[[ 1,  2],
#         [ 3,  4]],
#
#        [[11, 12],
#         [13, 14]]])
#
# print(np.unravel_index(i,Z.shape))
















































