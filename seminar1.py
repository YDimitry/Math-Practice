# шаг 14
# s = input()
# print(s[0]+s[1:].replace(s[0], '*'))

# шаг 13
# s = input()
# print(len(s) > 1 and s[:2]+s[-2:] or '')

# шаг 12
# n = int(input())
# print(f'Всего пончиков: {n<9 and n or "много"}')

# шаг 11
# def is_prime(n):
#     return all(map(lambda x: n%x,range(2,int(pow(n,0.5))+1)))
# print(is_prime(23))

# шаг 10
# def fib(n):
#     if n > 0:
#         return n == 1 and 1 or fib(n - 1) + fib(n - 2)
#     return 0
#
# print(fib(0))

# шаг 9
# def front_x(words):
#     x_filter = lambda inv: sorted(filter(lambda word: word.lower().startswith('x') ^ inv, words))
#     return x_filter(False) + x_filter(True)
#
# def front_x(words):
#     return sorted(words, key=lambda x: (x[:1] != 'x', x))
#
# print(front_x(['mix', 'extra', '', 'x-files', 'xyz', 'xapple', 'apple']))

# шаг 8
# def common(list_a, list_b):
#     return list(set(list_a) & set(list_b))
# list_a = [0, 2, 3, 4, 5, 19, 42]
# list_b = [0, 6, 19, 33, 42, 55, 66, 77, 99, 101, 256]
# print(common(list_a,list_b))

# шаг 7
# print(sum(filter(lambda x: (not x%5) and x%3,range(int(input())+1))))

# шаг 6
# def last_to_first(l):
#     return l[::-1]
#
# print(last_to_first([1, 1, 2, 3, 5, 8, 13, 21, 34]))


# шаг 5
# def even_elements(l):
#     return list(filter(lambda x: not x%2, l))
# print(even_elements( [1, 1, 2, 3, 5, 8, 13, 21, 34]))

# шаг 4
# def even_indeces(L):
#     return L[::2]
#
# print(even_indeces([1, 1, 2, 3, 5, 8, 13, 21, 34]))

# шаг 3
# from math import e
#
# der_e = lambda x, dx: (pow(e, x + dx) - pow(e, x)) / dx
#
#
# def def_e(x):
#     dx = 0.1
#     while abs(der_e(x, dx * 0.1) - der_e(x, dx)) > 1e-4:
#         dx *= 0.1
#     return round(der_e(x, dx),3)
#
# print(def_e(3))
# print(f'{pow(e,3):.3f}')

# шаг 2
# from math import atan
# # import numpy as np
# # x = np.arrange[11,2,0.01]
# f = lambda x: 2*atan(x)
#
# x = 1
# while f(x*10) - f(x) >1e-4:
#     x *= 10
#
# print(f'{f(x):.4f}')
