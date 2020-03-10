

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
