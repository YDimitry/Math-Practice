

event = "git fetch origin"
file_name = "git.log"

import os.path as path

events=[f"event 1 - '{event}'\n"]

if path.isfile(file_name):
    with open(file_name,'r', encoding="utf-8") as log:
        events = log.readlines()
        newevent =f"event {str(int(events[0].split()[1])+1)} - '{event}'\n"
        events.insert(0, newevent)

with open(file_name,'w', encoding="utf-8") as log:
    for e in events:
        log.write(e)

# with open('output.txt','w') as outf:
#     outf.write(input())


# import os.path as path
# fileOrDir = input()
#
# if path.isfile(fileOrDir):
#     with open(fileOrDir,'r',encoding="utf-8") as f:
#         print(f'CONTENT:\n{f.read()}')
# elif path.isdir(fileOrDir):
#     print('ERROR:\nЭто каталог, а не файл')
# else:
#     print('ERROR:\nФайл не существует')


# f = lambda seq: filter(methodcaller('isdigit'),seq)
# with open(sheet,'r',encoding="utf-8") as sht, open(mean,'r') as mn:
#     n = list(map(int, filter(methodcaller('isdigit'), map(lambda l: l.split()[-2], sht.readlines()))))
#     print('OK' if mn.read().rstrip() == str(round(sum(n)/len(n))) else 'ERROR')

# with open(input(),'r')as f:
#     print(f.readlines()[-1].rstrip())


# with open(input(),'r')as f:
#     print(sum(map(int,f.readlines())))


# def factorial(n):
#     return reduce(mul, range(1,n+1),1)
#
# def sf(n):
#     return reduce(mul,map(factorial, range(1,n+1)),1)

# def translate(i,n):
#     r = str(i%n)
#     return translate(i//n, n) + r if i // n else r

# def Kfactorial(n, k=1):
#     return reduce(mul, range(n, 1, -k), 1)

# def dfactorial(n):
#     return reduce(mul, range(1+(not n%2), n+1, 2),1)
#
# print(dfactorial(4))


# n = abs(4)
# print(*map(curry(flip(pow))(3),range(1,n+1)),sep='\n')


# n = int(input())
#
# for i in range(2,n+1):
#     if not n%i:
#         break
# print(i)

# print(*filter(lambda x: x[0]!='*', input().split()),sep='\n')

# print(sum(map(int,iter(input,'The End'))))

# print(*map(curry(flip(pow))(2), range(0,int(input()),2)),sep='\n')

# typ = input()
# if typ == 'str':
#     s = input()
#     print(s and s or 'Empty String')
# elif typ =='int':
#     a = list(map(int,[input() for _ in range(2)]))
#     print(sum(a) if any(a) else 'Empty Ints')
# elif typ =='list':
#     s = input()
#     print(s and s.split()[-1] or 'Empty List')
# else:
#     print('Unknown type')


# b = int(input())
# print(b and round(int(input())/b,1) or 'Division by zero!')


# input = "['mix', 'extra', '', 'x-files', 'xyz', 'xapple', 'apple']"
# L = [s.replace("'",'') for s in input()[1:-1].split(', ')]


# b1 = 'hello world'
# b2 = b1[::2]
# print(b2)
# print('$'.join([input() for _ in range(2)]))
# print(sum(map(int,input().split()))

# s = input().split()
# print(len(s),s.count('one'))
# print('-$-'.join(input().split()[::-1]))
# s = input().split()
# print(s[1:2],s[-2])

# print(*{input().split('&')})

# print('#'.join([sum(map(int,input.split())) for _ in range(2)]))

# Задача фон Неймана о мухе и поездах
# L,v1,v2,vm = (int(input()), for _ in range(4))
#
# print(L/(v1+v2)*vm)


# додекаэдр
# v = 7.66*a^2
# s = 1.422 *a
# a = 2
# s = pow(5,0.5)*pow((5+2*pow(5,0.5)),0.5)/4 * pow(a,2)
# v = (15+7*pow(5,0.5))/4 * pow(a,3)
# print(round(12*s,2), round(v,2))



# площадь шестиугольника 2
# равносторонний тр. (a^2*√3)/4
# квадрат a^2
# шестиугольник (3*√3 a^2)/ 2

# a = int(input())
# print(round(3*pow(a,2)*pow(3,0.5)/2 +3*pow(a,2)+6*pow(a/2,2)*pow(3,0.5)/4))

# площадь шестиугольника
# a = int(input())
# s = lambda a: pow(a,2)*pow(3,0.5)/4
# print(round(s(a*3)+2*s(a)))

# площадь ромба

# x = map(float,[input() for _ in range(2)])
# s = mul(*x)/2
# print(*[int(s),round(s,1),s],sep='\n')

# площадь треугольника
# x = [int(input()) for _ in range(3)]
# perim = lambda a: sum(a)
# p = lambda a: perim(a)/2
# s = lambda a: pow(p(a)*(p(a)-a[0])*(p(a)-a[1])*(p(a)-a[2]),0.5)
# print(perim(x), s(x),sep='\n')


# x = [int(input()) for _ in range(2)]
# op = [add, sub, flip(sub),truediv, flip(mod), pow]
# print(*map(partial(flip(reduce)(a)), op),sep='\n')
# print(*map(lambda f: f(*x),op),sep='\n')
# print((op,repeat((7,9))))
# print(partial(reduce)(add,(7,9)))
# print(*reduce(partial(map,add),zip((1,2,3),(1,1,1)),(0,0)))

# with open('file.txt','r') as data:
#      writefile, textfile,n = [s.rstrip() for s in data]
#
# with open(writefile,'a') as outf, open(textfile,'r') as text:
#     t = text.readlines()
#     outf.write(t[int(n)].lower())

# from scipy.constants import c, h, e, golden

# def lam(U):
#     return h*c/(e*U)

# def counter(T):
#     return len(sorted(sorted(T, key=lambda e:len(e)), key=lambda e: len(set(e.lower())))[-1])
# def counter(T):
#     return max(map(lambda s: (len(set(s.lower())), len(s)), T))
# print(set('ABBA'))

# print(reduce(lambda a,b: abs(sub(*b))==1 and L.index(b[0]) or 0, sliding_window(2, L),(0, 0)))
# import numpy as np
#
# a = np.array([1,0,3])
# b = np.array([0,2,1])
#
# c = 2*a-3*b
#
# M = np.array([a,b,c])
# print(M)
# print(np.linalg.matrix_rank(M))
