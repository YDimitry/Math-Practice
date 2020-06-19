# Задача 1.1 - кучки бумажек (можно или нет)

# inp = '3 2 3'
# heaps = list(map(int,inp.split()))
#
# if len(heaps)<2:
#     print('Ошибка. Кучек слишком мало, чтобы можно было решить задачу.')
# elif (len(heaps) == 2 and heaps[0] == heaps[1]) or (len(heaps) > 2 and not sum(heaps)%2) or (sum(heaps)%2 and len(heaps)%2):
#     print('Кучки можно уравнять')
# else:
#     print('Кучки нельзя уравнять')


# Задача 1.2 - Кучки бумажек (число ходов)
# inp = '1 7 7'
# heaps = list(map(int,inp.split()))
# total = sum(heaps)
# num = len(heaps)
# m = 0
# if len(heaps)<2:
#     print('Ошибка. Кучек слишком мало, чтобы можно было решить задачу.')
# elif (num == 2 and heaps[0] == heaps[1]) or (num > 2 and not total%2) or (total%2 and num%2):
#     while len(set(heaps)) != 1:  # not all(map(lambda x: x == heaps[0], heaps[1:])):
#         heaps.sort()
#         heaps[0] +=1
#         heaps[1] +=1
#         m += 1
#     print(m, heaps[0])
# else:
#     print('Кучки нельзя уравнять')

# Задача 2 - Можно ли замостить доминошками фигуру
# inp = '4 4'
# n, m = map(int,inp.split())
# print(('Замостить нельзя','Замостить можно')[n%2 ^ m%2])


# Задача 3 - сумма цифр на километровых столбах
# from functools import partial
# from toolz import compose
#
# a = 100
#
# dist = a
# print(*map(compose(lambda s: s == a, sum, partial(map,compose(sum,partial(map,int),str))),zip(range(a+1),reversed(range(a+1)))))
# while True:
#     sum_dist = sum(map(int, str(dist)))
#     if sum_dist == a and all(map(compose(lambda s: s == a, sum, partial(map,compose(sum,partial(map,int),str))),zip(range(dist+1),reversed(range(dist+1))))):
#         break
#     dist += 1
#
# print(dist)

# Задача 4.1 - пятнашки (чётность перестановки)

def parity(b):
# b = list(map(int,a.split()))
    c = 0
    for i,n in enumerate(b):
        for m in b[i+1:]:
            if n>m:
                # print((n,m))
                c +=1
    # print(c)
    return [1,-1][bool(c%2)]

# Задача 4.2 - пятнашки (возможность выигрыша из текущей позиции)
# a = []
# for i in range(4):
#     # a.extend(map(int, i%2 and reversed(input().split()) or input().split()))
#     a.extend(map(int, input().split()))
#
# b = (1, 2, 3, 4, 8, 7, 6, 5, 9, 10, 11, 12, 15, 14, 13)
# print(a)
# print(parity(a))
# print(b)
# print(parity(b))
# if parity((1, 2, 3, 4, 8, 7, 6, 5, 9, 10, 11, 12, 15, 14, 13)) == parity(a):
#     print('Бинго!')
# else:
#     print('Не повезло...')


# Задача 4.3 - пятнашки (на поле произвольного размера)
#
# n,m = map(int,input().split())
# a = []
# for _ in range(n):
#     a.extend(map(int, input().split()))
#
# tmp = list(range(1, n*m))
# b = []
# for i in range(n):
#     b.extend(i % 2 and reversed(tmp[i*m:i*m+m]) or tmp[i*m:i*m+m])
#
# print(("Не повезло...","Бинго!")[parity(a) == parity(b)])



def fib_gen(n):
    a,b = 0,1
    while n:
        if not a % 2:
            yield a
            n -=1
        a, b = b, a + b

def f(n):
    return list(fib_gen(n))

print(f(4))














