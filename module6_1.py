import numpy as np
# задача 1
# inp = "1, 2, 3, 4, 5.0, 6, 7, 8, 9, 10"
# lst = list(map(float, inp.split(',')))
# V1 = np.array(lst)
# V2 = np.array(lst[-2])
# V3 = np.array(lst[::-1])
# V4 = np.array(lst[::3])
# V5 = np.array(range(len(lst)))

# задача 2
# inp = ["1, 2, 3, 4","10, 20, 30, 40"]
# a,b = [list(map(int,a.split(','))) for a in inp]

# a,b = [list(map(int,input().split(','))) for _ in range(2)]

# V1 = np.array(a)
# V2 = np.array(b)
# V3 = V1 + V2
# V4 = V1[::2] * V2[::-2]
#
# print(V1,V2,V3,V4, sep='\n')

# задача 3
# inp = ['1, 2, 3, 4, 5, 6','1, 2, 3, 4']
# a,b = [list(map(int,a.split(','))) for a in inp]

# a,b = [list(map(int,input().split(','))) for _ in range(2)]
# V = np.array(a)
# V = V[V % b[-2] == 0] / 3
#
# print(V)

# задача 4

# A1 = np.array((-1, 1))
# A2 = np.array((2, 5))
# A3 = np.array((5, -3))
# A1 = np.array((-1, 2))
# A2 = np.array((2, 3))
# A3 = np.array((5, 4))
#
# a = (sum((A1-A2)**2))**0.5
# b = (sum((A2-A3)**2))**0.5
# c = (sum((A3-A1)**2))**0.5
#
# p = (a+b+c)/2
#
# s = round((p*(p-a)*(p-b)*(p-c))**0.5,4)
# print(s)

# задача 5
np.set_printoptions(precision=2)
np.set_printoptions(suppress=True)
M1 = np.array((
    (1., 2., 3., 0.),
    (4., 5., 6., 0.),
    (0., 1., 1., 6.),
    (7., 8., 9., 0.)
))

M2 = M1.copy()
M2[-2] = np.sin(M1[-2] * np.pi/6)
# print(M2)
M2 = M2.T
M2[-2] = np.exp(M2[-2])
M2 = M2.T
# print()
# M2[-2][-2] = np.exp(np.sin(M2[-2][-2]*np.pi/6))
# print(np.round(M2,2))
# print(M2)

# print(np.exp())










































































