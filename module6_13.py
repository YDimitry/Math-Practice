import numpy as np
# задача 1.1
# n = 2
# obj = map(float, input().split())
# m = np.array([input().split() for _ in range(3)], dtype=float)
# M1 = m[:,:-1]
# V1 = m[:,-1]
# print(*np.linalg.solve(M1,V1).flatten())

# задача 1.2
# if np.linalg.det(M1):
#     print(*np.linalg.solve(M1,V1).flatten())
# else:
#     print("Матрица системы вырожденная")
# задача 2

# задача 3

# задача 4

# задача 4.1
# x+y=20
# y-x=4
# задача 4.2
# a, b = map(int, input().split())
# M1 = np.array([[1,1],[1,-1]])
# V1 = np.array([[a],[b]])
#
# if a > b and np.linalg.det(M1) and not((a+b)%2):
#     print(*np.linalg.solve(M1, V1).flatten().astype(int))
# else:
#     print('Такой класс не существует')


# print(np.linalg.matrix_rank(M1))
# print(np.linalg.matrix_rank(np.append(M1,V1, axis=1)))
# print(np.linalg.solve(M1,V1).dtype)

# задача 4.3

# задача 4.4

# задача 5
# n = int(input())
# m = np.array([input().split() for _ in range(n)], dtype=float)
# x = np.tile(m[:,:-1],(1,n))
# a = np.tile(np.arange(n), (n,1))
# print(*np.linalg.solve(x**a, m[:,-1]))

# задача 6
# Для следующего задания используйте 6 точек: (0,1), (1,1), (2,25), (-1,1), (-2,-23), (0.5,0.90625)

m = np.array([(0,1), (1,1), (2,25), (-1,1), (-2,-23), (0.5,0.90625)])
n = m.shape[0]
x = np.tile(m[:,:-1],(1,n))
a = np.tile(np.arange(n), (n,1))
c = np.linalg.solve(x**a, m[:,-1])

def f(x, c):
    return sum([c_i * x**n for n, c_i in enumerate(c)])

















