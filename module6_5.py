import numpy as np

# 22 Нормализация
# Y = np.array([[99, 11, 55],[33, 66, 99]])
# mu = np.mean(Y)
# sig = np.std(Y)
# Z = np.around((Y-mu)/sig,2)
# print(Z)

# 24.1 Скалярное произведение векторов
# A = np.array([1, 3, 5, 7, 9])
# B = np.array([-2, 4, -6, 8, -10])
#
# Z = sum(A * B)
# print(Z)

# 24.2 Умножение матриц
# A = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])
# B = np.array([
#     [11.5],
#     [12.5],
#     [13.5]
# ])
#
# A = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])
# B = np.array([
#     [11.5, 12.5, 13.5]
# ])
# try:
#     Z = np.dot(A,B)
# except ValueError:
#     print("Упс! Что-то пошло не так...")

# задача 25
# Z = np.arange(11)
# Z = np.array([-10, -5, 0, 5, 10])
# Y = np.where((Z > 3) & (Z < 9), -Z, Z)
#
# print(Z)
# print(Y)

# задача 29
# A = np.array([-3.1, -5.9, 0, 2.2, 9.8])
# Z = np.copysign(np.ceil(np.abs(A)),A)
# print(Z)

# задача 30
# A = np.array([0, 9, 7, 1, 3, 7, 5, 2, 5, 1])
# B = np.array([3, 1, 3, 7, 4, 1, 8, 1, 1, 8])
# A = np.array([1, 2, 3, 4, 5])
# B = np.array([-5, -4, -3])
# Z = np.intersect1d(A,B)
# print(Z)














































