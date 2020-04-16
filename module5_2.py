# 1.1 Предел функции

f = lambda x: (2*x**2 - 3*x - 5) / (3*x**2 + x + 1)

def lim(f,x=10,step=10,pres=1e-4):
    while abs(f(x)-f(x*step))>pres:
        print(f(x)-f(x*step))
        x *= step
    return f(x)

# print(round(lim(f,x=-10),3))
# print(round(lim(f,x=-10),3))

# 1.2 Предел функции
from math import pi, sin, cos,atan, exp
f = lambda x: sin(pi*x/2) / x

# r = lim(f,x=1,step=10,pres=1e-20)
# print(round(r,3))

# 2. Производная

def derivative(f, x0=0):
    der = lambda f, dx: (f(x0+dx) - f(x0)) / dx
    dx = 0.1
    while abs(der(f,dx*0.1)-der(f,dx)) > 1e-4:
        dx *= 0.1
    return round(der(f, dx), 3)

# print(derivative(exp, 1))

# 3. Вытянуть многомерный список
def list_pull(L):
    res = []
    for el in L:
        if isinstance(el,list):
            res.extend(list_pull(el))
        else:
            res.append(el)
    return res

# 4. Скопировать многомерный список без deepcopy
def list_copy(L):
    res = []
    for el in L:
        if isinstance(el,list):
            res.append(list_copy(el))
        else:
            res.append(el)
    return res

# print(list_copy([1,2,[3,3,3,[4,4,4]],5,5,[[[6]]]]))

# A. verbing
def verbing(s):
    if len(s)<3:
        return s
    if s.endswith('ing'):
        return s+'ly'
    return s + 'ing'

# B. front_back
from math import ceil
def front_back(a,b):
    def divide(s):
        center = ceil(len(s) / 2)
        return s[:center],s[center:]
    a_front,a_back,b_front,b_back = *divide(a), *divide(b)
    return a_front+b_front+a_back+b_back

# print(front_back('abccer','xy'))

# C1. mimic_dict
def mimic_dict(string):
    s = ""
    d = {}
    for word in string.split():
        lst = d.setdefault(s,[])
        if word not in lst:
            lst.append(word)
        s = word
    return d

a = """We are not what we should be
We are not what we need to be
But at least we are not what we used to be
  -- Football Coach"""
print(mimic_dict(a))
import random

def print_mimic(mimic_dict, word):
    def word_gen():
        nonlocal word
        for _ in range(200):
            yield word
            word = random.choice(mimic_dict.get(word, mimic_dict[""]))
    return ' '.join(word_gen())

print(print_mimic(mimic_dict(a),'we'))




