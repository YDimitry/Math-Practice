# 4.7 Энигма
import re
# step 2
rot = {1: ('AELTPHQXRU', 'BKNW', 'CMOY', 'DFG', 'IV', 'JZ', 'S'),
     2: ('FIXVYOMW', 'CDKLHUP', 'ESZ', 'BJ', 'GR', 'NT', 'A', 'Q'),
     3: ('ABDHPEJT', 'CFLVMZOYQIRWUKXSG', 'N')}

refl = {1: ('AY', 'BR', 'CU', 'DH', 'EQ', 'FS', 'GL', 'IP', 'JX', 'KN', 'MO', 'TZ', 'VW'),
     2: ('AF', 'BV', 'CP', 'DJ', 'EI', 'GO', 'HY', 'KR', 'LZ', 'MX', 'NW', 'TQ', 'SU')}

stepping2 = {1:17, 2:5, 3:22, 4:10, 5:0}


def rotor_reflector(symbol,dic,n,reverse=False):
    seq = list(*filter(lambda s: symbol in s, dic.get(n, [symbol])))
    return seq[(seq.index(symbol)+1-2*reverse)%len(seq)]

# def rotor(symbol, n, reverse=False):
#     return rotor_reflector(symbol,rot,n,reverse)

# step 3
# def reflector(symbol, n):
#     return rotor_reflector(symbol,refl,n)


# step 5
def enigma1(text, ref, rot1, rot2, rot3):
    s = re.sub(r'\W', '', text.upper())
    rotors = [rot3, rot2, rot1]

    def disks(symb, rev=False):
        d = 1 - 2 * rev
        for i in rotors[::d]:
            symb = rotor_reflector(symb, rot, i, rev)
        return symb

    return ''.join(map(lambda a:disks(rotor_reflector(disks(a), refl, ref), True), s))


def enigma2(text, ref, rot1, shift1, rot2, shift2, rot3, shift3):
    s = re.sub(r'\W', '', text.upper())
    shifts = [shift3, shift2, shift1]
    rotors = [rot3, rot2, rot1]

    def shift(c, n, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        return alphabet[(alphabet.index(c) + n) % len(alphabet)]

    def disks(symbol, rev=False):
        prev_shift = 0
        d = 1-2*rev
        for n, i in zip(rotors[::d], shifts[::d]):
            symbol = rotor_reflector(shift(symbol,i-prev_shift), rot, n, rev)
            prev_shift = i
        symbol = shift(symbol, -prev_shift)
        return symbol

    return ''.join(map(lambda a: disks(rotor_reflector(disks(a),refl,ref),True), s))


def enigma3(text, ref, rot1, shift1, rot2, shift2, rot3, shift3):
    s = re.sub(r'\W', '', text.upper())
    shifts = [shift3, shift2, shift1]
    rotors = [rot3, rot2, rot1]
    step = lambda n: (n + 1) % 26

    def shift(c, n, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        return alphabet[(alphabet.index(c) + n) % len(alphabet)]

    def move_disks():
        shifts[0] = step(shifts[0])
        for i in range(len(shifts) - 1):
            if shifts[i] == stepping[rotors[i]] or (not i and shifts[i + 1] + 1 == stepping[rotors[i + 1]]):
                shifts[i + 1] = step(shifts[i + 1])
            else:
                break

    def disks(symbol, rev=False):
        prev_shift = 0
        d = 1-2*rev
        for n, i in zip(rotors[::d], shifts[::d]):
            symbol = rotor_reflector(shift(symbol,i-prev_shift), rot, n, rev)
            prev_shift = i
        symbol = shift(symbol, -prev_shift)
        return symbol

    def enc(a):
        move_disks()
        # print(a,*shifts,end=' ')
        a = disks(rotor_reflector(disks(a),refl,ref),True)
        # print(a)
        return a

    return ''.join(map(enc, s))

def enigma(text, ref, rot1, shift1, rot2, shift2, rot3, shift3, pairs=""):
    s = re.sub(r'\W', '', text.upper())
    shifts = [shift3, shift2, shift1]
    rotors = [rot3, rot2, rot1]
    step = lambda n: (n + 1) % 26
    pairs = pairs.upper().split()

    def shift(c, n, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        return alphabet[(alphabet.index(c) + n) % len(alphabet)]

    def move_disks():
        shifts[0] = step(shifts[0])
        for i in range(len(shifts) - 1):
            if shifts[i] == stepping2[rotors[i]] or (not i and shifts[i + 1] + 1 == stepping2[rotors[i + 1]]):
                shifts[i + 1] = step(shifts[i + 1])
            else:
                break

    def disks(symbol, rev=False):
        prev_shift = 0
        d = 1-2*rev
        for n, i in zip(rotors[::d], shifts[::d]):
            symbol = rotor_reflector(shift(symbol,i-prev_shift), rot, n, rev)
            prev_shift = i
        symbol = shift(symbol, -prev_shift)
        return symbol

    def commutate(a):
        pair = list(filter(lambda p: a in p, pairs))
        if len(pair) > 1:
            raise ValueError('Извините, невозможно произвести коммутацию')
        if pair:
            return pair[0][(pair[0].index(a) + 1) % 2]
        return a

    def enc(a):
        move_disks()
        return commutate(disks(rotor_reflector(disks(commutate(a)),refl,ref),True))

    try:
        return ''.join(map(enc, s))
    except ValueError as e:
        return e

# step 11
class Enigma:
    __alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    __rotor = {1: ('AELTPHQXRU', 'BKNW', 'CMOY', 'DFG', 'IV', 'JZ', 'S'),
           2: ('FIXVYOMW', 'CDKLHUP', 'ESZ', 'BJ', 'GR', 'NT', 'A', 'Q'),
           3: ('ABDHPEJT', 'CFLVMZOYQIRWUKXSG', 'N')}

    __refl = {1: ('AY', 'BR', 'CU', 'DH', 'EQ', 'FS', 'GL', 'IP', 'JX', 'KN', 'MO', 'TZ', 'VW'),
            2: ('AF', 'BV', 'CP', 'DJ', 'EI', 'GO', 'HY', 'KR', 'LZ', 'MX', 'NW', 'TQ', 'SU')}

    __stepping = {1: 17, 2: 5, 3: 22, 4: 10, 5: 0}


    def __init__(self, reflector=1, rotors=[3,2,1], shifts=[0,0,0], pairs=""):
        self.__shifts = shifts[::]
        self.__rotors = rotors
        self.__pairs = pairs.upper().split()
        self.__reflector_type = reflector

    def __rotor_reflector(self, symbol, rotor_or_refl, n, reverse=False):
        seq = list(*filter(lambda s: symbol in s, rotor_or_refl.get(n, [symbol])))
        return seq[(seq.index(symbol) + 1 - 2 * reverse) % len(seq)]

    def __shift(self, char, key):
        return self.__alphabet[(self.__alphabet.index(char) + key) % len(self.__alphabet)]

    def __move_disks(self):
        step = lambda n: (n + 1) % 26
        self.__shifts[0] = step(self.__shifts[0])
        for i in range(len(self.__shifts) - 1):
            if self.__shifts[i] == self.__stepping[self.__rotors[i]] or (
                    not i and self.__shifts[i + 1] + 1 ==
                    self.__stepping[self.__rotors[i + 1]]):

                self.__shifts[i + 1] = step(self.__shifts[i + 1])
            else:
                break

    def __pass_through_disks(self, symbol, reverse=False):
        prev_shift = 0
        d = 1-2*reverse
        for n, i in zip(self.__rotors[::d], self.__shifts[::d]):
            symbol = self.__rotor_reflector(self.__shift(symbol,i-prev_shift), self.__rotor, n, reverse)
            prev_shift = i
        symbol = self.__shift(symbol, -prev_shift)
        return symbol

    def __commutate_pair(self, symbol):
        pair = list(filter(lambda p: symbol in p, self.__pairs))
        if len(pair) > 1:
            raise ValueError('Извините, невозможно произвести коммутацию')
        if pair:
            return pair[0][(pair[0].index(symbol) + 1) % 2]
        return symbol

    def encode_symbol(self, symbol):
        self.__move_disks()
        c = self.__pass_through_disks(self.__commutate_pair(symbol[:1]))
        c = rotor_reflector(c,self.__refl,self.__reflector_type,reverse=True)
        return self.__commutate_pair(self.__pass_through_disks(c,reverse=True))

    def encode_text(self,text):
        string = re.sub(r'\W', '', text.upper())
        try:
            return ''.join([self.encode_symbol(symbol) for symbol in string])
        except ValueError as e:
            return e


def enigma(text, ref, rot1, shift1, rot2, shift2, rot3, shift3, pairs=""):
    enigm = Enigma(ref, [rot3, rot2, rot1], [shift3, shift2, shift1], pairs)
    return enigm.encode_text(text)

# print(enigma('Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 1, 1, 0, 2, 0, 3, 0, 'AC qd'))

# step 9
class Enigma:
    __alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    __rotor = {1: ('AELTPHQXRU', 'BKNW', 'CMOY', 'DFG', 'IV', 'JZ', 'S'),
           2: ('FIXVYOMW', 'CDKLHUP', 'ESZ', 'BJ', 'GR', 'NT', 'A', 'Q'),
           3: ('ABDHPEJT', 'CFLVMZOYQIRWUKXSG', 'N')}

    __refl = {1: ('AY', 'BR', 'CU', 'DH', 'EQ', 'FS', 'GL', 'IP', 'JX', 'KN', 'MO', 'TZ', 'VW'),
            2: ('AF', 'BV', 'CP', 'DJ', 'EI', 'GO', 'HY', 'KR', 'LZ', 'MX', 'NW', 'TQ', 'SU')}

    __stepping = {1: 17, 2: 5, 3: 22, 4: 10, 5: 0}

    def __init__(self, reflector=1, rotors=[3,2,1], shifts=[0,0,0]):
        self.__shifts = shifts[::]
        self.__rotors = rotors
        self.__reflector_type = reflector

    def __rotor_reflector(self, symbol, rotor_or_refl, n, reverse=False):
        seq = list(*filter(lambda s: symbol in s, rotor_or_refl.get(n, [symbol])))
        return seq[(seq.index(symbol) + 1 - 2 * reverse) % len(seq)]

    def __shift(self, char, key):
        return self.__alphabet[(self.__alphabet.index(char) + key) % len(self.__alphabet)]

    def __move_disks(self):
        step = lambda n: (n + 1) % 26
        self.__shifts[0] = step(self.__shifts[0])
        for i in range(len(self.__shifts) - 1):
            if self.__shifts[i] == self.__stepping[self.__rotors[i]] or (
                    not i and self.__shifts[i + 1] + 1 ==
                    self.__stepping[self.__rotors[i + 1]]):

                self.__shifts[i + 1] = step(self.__shifts[i + 1])
            else:
                break

    def __pass_through_disks(self, symbol, reverse=False):
        prev_shift = 0
        d = 1-2*reverse
        for n, i in zip(self.__rotors[::d], self.__shifts[::d]):
            symbol = self.__rotor_reflector(self.__shift(symbol,i-prev_shift), self.__rotor, n, reverse)
            prev_shift = i
        symbol = self.__shift(symbol, -prev_shift)
        return symbol

    def encode_symbol(self, symbol):
        self.__move_disks()
        c = self.__pass_through_disks(symbol[:1])
        c = self.__rotor_reflector(c,self.__refl,self.__reflector_type,reverse=True)
        return self.__pass_through_disks(c,reverse=True)

    def encode_text(self,text):
        string = re.sub(r'\W', '', text.upper())
        try:
            return ''.join([self.encode_symbol(symbol) for symbol in string])
        except ValueError as e:
            return e

def enigma(text, ref, rot1, shift1, rot2, shift2, rot3, shift3):
    enigm = Enigma(ref, [rot3, rot2, rot1], [shift3, shift2, shift1])
    return enigm.encode_text(text)

# print(enigma('AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA', 1, 2, 3, 2, 3, 2, 3))

# step 7
class Enigma:
    __alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    __rotor = {1: ('AELTPHQXRU', 'BKNW', 'CMOY', 'DFG', 'IV', 'JZ', 'S'),
           2: ('FIXVYOMW', 'CDKLHUP', 'ESZ', 'BJ', 'GR', 'NT', 'A', 'Q'),
           3: ('ABDHPEJT', 'CFLVMZOYQIRWUKXSG', 'N')}

    __refl = {1: ('AY', 'BR', 'CU', 'DH', 'EQ', 'FS', 'GL', 'IP', 'JX', 'KN', 'MO', 'TZ', 'VW'),
            2: ('AF', 'BV', 'CP', 'DJ', 'EI', 'GO', 'HY', 'KR', 'LZ', 'MX', 'NW', 'TQ', 'SU')}

    def __init__(self, reflector=1, rotors=[3,2,1], shifts=[0,0,0]):
        self.__shifts = shifts[::]
        self.__rotors = rotors
        self.__reflector_type = reflector

    def __rotor_reflector(self, symbol, rotor_or_refl, n, reverse=False):
        seq = list(*filter(lambda s: symbol in s, rotor_or_refl.get(n, [symbol])))
        return seq[(seq.index(symbol) + 1 - 2 * reverse) % len(seq)]

    def __shift(self, char, key):
        return self.__alphabet[(self.__alphabet.index(char) + key) % len(self.__alphabet)]

    def __pass_through_disks(self, symbol, reverse=False):
        prev_shift = 0
        d = 1-2*reverse
        for n, i in zip(self.__rotors[::d], self.__shifts[::d]):
            symbol = self.__rotor_reflector(self.__shift(symbol,i-prev_shift), self.__rotor, n, reverse)
            prev_shift = i
        symbol = self.__shift(symbol, -prev_shift)
        return symbol

    def encode_symbol(self, symbol):
        c = self.__pass_through_disks(symbol[:1])
        c = self.__rotor_reflector(c,self.__refl,self.__reflector_type,reverse=True)
        return self.__pass_through_disks(c,reverse=True)

    def encode_text(self,text):
        string = re.sub(r'\W', '', text.upper())
        try:
            return ''.join([self.encode_symbol(symbol) for symbol in string])
        except ValueError as e:
            return e

def enigma(text, ref, rot1, shift1, rot2, shift2, rot3, shift3):
    enigm = Enigma(ref, [rot3, rot2, rot1], [shift3, shift2, shift1])
    return enigm.encode_text(text)

print(enigma('AYIQQLXZMFHQUHQCH', 1, 1, -1, 2, 2, 3, -1))
# pairs = ''.upper().split()
#
# def switch_swymbol(a):
#     pair = list(filter(lambda p: a in p, pairs))
#     if len(pair)>1:
#         raise ValueError('Извините, невозможно произвести коммутацию')
#     if pair:
#         return pair[0][(pair[0].index(a)+1)%2]
#     return a
# try:
#     print(switch_swymbol('S'))
# except ValueError as e:
#     print(e)
exit()

# 4.6 Аве, Цезарь!
import random

from collections import deque
from functools import partial
from operator import methodcaller, itemgetter
from toolz import curry, flip, get


# step 11

k = 'ethosnairfdlmbyguvcp'
v = '8;4‡)*56(1†092:3?¶-.'
# z = lambda rev: rev and flip(zip) or zip
# dic = lambda a, b: lambda c: b[a.index(c)]


def kidds_encryption(text, reverse=False):
    s = re.sub(r'\W', '', text.lower())
    d = {k: v for k, v in zip(*[(k, v), (v, k)][reverse])}
    # e = dic(*[(k, v), (v, k)][reverse])
    # print(d)
    return ''.join(map(lambda x: d.get(x,''), reverse and text or s))

# t = "the death's-head a bee line from the"
# t = ";48†85;4)485†528806*81(‡9;48"
# t = 'XxL ,L, LxX'
# print(kidds_encryption(t))
# print(flip(get)(d)('d'))
# step 9

def disc_generator(alphabet,n=1):
    random.seed(42)
    for _ in range(n):
        res = list(alphabet)
        random.shuffle(res)
        yield ''.join(res)

# step 10

def jefferson_encryption(text, discs, step, reverse=False):
    s = re.sub(r'\W', '', text.upper())

    def caesar(text,disks,key,rev):
        res = ''
        for i,c in enumerate(text):
            res += discs[i][(discs[i].index(c) + key*(1-2*rev)) % len(discs[i])]
        return res

    def enc_gen():
        m, n = 0, len(discs)
        while m < len(s):
            yield caesar(s[m:n], discs, step, reverse)
            m = n
            n *= 2

    return ''.join(enc_gen())


# clear_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# n = 36
# text = 'Съешь еще этих мягких французских булок. Кстати, в этом тексте пришлось заменить одну букву...'
# text = 'КЗТХРЪФФЗЗЦРНЧНШНПЩНИЛЙЮНГХРЪВНЩЬВПКЪЭЧНЛЫЛШРЗБШКЫЛСЬЪЛИЮЕЧДОАНЙХЪБЗИЙЫУСТОЭ'
# discs = list(disc_generator(clear_alphabet,n))
#
# print(jefferson_encryption(text,discs,13,True))


# step 6
def jarriquez_encryption(text, key, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ', reverse=False):
    s = re.sub(r'\W', '', text.upper())

    def key_gen(key):
        i = 0
        s = str(key)
        while True:
            yield int(s[i % len(s)])
            i += 1

    k = key_gen(key)
    return ''.join(map(lambda x: alphabet[(alphabet.index(x)+next(k)*(1-2*reverse))%len(alphabet)], s))

# step 8

# print('encripted'.upper() in jarriquez_encryption('UUNEFWKXKVUEECMDVLPRUQQYCYTIHWUKPZ',26101986,reverse=True))

# text = """ТЛБЛДУЭППТКЛФЧУВНУПБКЗИХТЛТТЫХНЛОИНУВЖММИНПФНПШОКЧЛЕРНТФНАХЖИДМЯКЛТУБЖИУЕЖЕАХЛГЩЕЕ
# ЪУВНГАХИЯШПЙАОЦЦПВТЛБФТТИИНДИДНЧЮОНЯОФВТЕАТФУШБЛРЮЮЧЖДРУУШГЕХУРПЧЕУВАЭУОЙБДБНОЛСКЦБ
# САОЦЦПВИШЮТППЦЧНЖОИНШВРЗЕЗКЗСБЮНЙРКПСЪЖФФШНЦЗРСЭШЦПЖСЙНГЭФФВЫМЖИЛРОЩСЗЮЙФШФДЖО
# ИЗТРМООЙБНФГОЩЧФЖООКОФВЙСЭФЖУЬХИСЦЖГИЪЖДШПРМЖПУПГЦНВКБНРЕКИБШМЦХЙИАМФЛУЬЙИСЗРТЕС
# """.replace('\n','')

# keywords = list(map(methodcaller('upper'),['алмаз','Дакост','Жаррик']))
# alph = sorted(set(text))

# 261086
def brute_jarriquez():
    found = False
    # for k in range(1000000,99,-1):
    for i in range(1,10):
        k = int(str(i)+'61086')
        if found:
            break
        print(k)
        denc = jarriquez_encryption(text, k, alph, True)
        for keyword in keywords:
            if keyword in denc:
                print(f'found key! {k} for {keyword}')
                print(denc)
                # if not (input('Continue?')=='y'):
                #     found = True
                #     break


# step 4
def bruteforce(text, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    for i in range(-1,-len(alphabet)-1,-1):
        print(*map(lambda x:alphabet[alphabet.index(x)+i], text),sep='')


# step 3
def caesar(text, key, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    s = list(re.sub(r'\W', '', text.upper()))
    return ''.join(map(lambda x: alphabet[(alphabet.index(x)+key) % len(alphabet)], s))

# step 3
def caesar(text, key):
    return ''.join(map(lambda x: chr(65+(ord(x)-65+key)%26), list(re.sub(r'\W', '', text.upper()))))


# 4.5 Таблица умножения двузначных чисел от "Мудреца"
# from functools import reduce
# from itertools import product


# def wisdom_multiplication(x, y, length_check=True):
#     a, b = (100-x), (100-y)
#     chk = lambda x: len(str(x))<2 and '0' or ''
#     return int(str(100 - (a+b))+chk(a*b)*length_check+str(a*b))
#
# def simple_multiplication(x, y):
#     a, b = (100-x), (100-y)
#     return (100 - (a + b))*100+(a*b)
#
# def multiplication_check(x, y, length_check):
#     # if wisdom_multiplication(x, y, length_check) != str(x*y):
#     #     print(x,y, wisdom_multiplication(x, y, length_check), x*y)
#     return wisdom_multiplication(x, y, length_check) == x*y
#
# def multiplication_check_list(start=10, stop=99):
#     a,b = reduce(lambda a,b: multiplication_check(*b) and (a[0]+1,a[1]) or (a[0],a[1]+1), product(range(start,stop+1), repeat=2),(0,0))
    # a, b = 0, 0
    # for x in range(start,stop+1):
    #     for y in range(start,stop+1):
    #         chk = multiplication_check(x,y)
    #         a, b = a+chk, b+ (not chk)
    # print(f'Правильных результатов: {a}\nНеправильных результатов: {b}')

# def multiplication_check_list(start=10, stop=99, length_check=True):
#     a,b = reduce(lambda a,b: multiplication_check(*b, length_check) and (a[0]+1,a[1]) or (a[0],a[1]+1), product(range(start,stop+1), repeat=2),(0,0))
#     print(f'Правильных результатов: {a}\nНеправильных результатов: {b}')

# def multiplication_check_list(start=10, stop=99):
#     for x in range(start,stop+1):
#         for y in range(start,stop+1):
#             s = multiplication_check(x,y, False)+multiplication_check(x,y, True)
#             print(f'{x}x{y} = {x*y} {wisdom_multiplication(x,y,False)} {wisdom_multiplication(x,y)}',s)

# import pandas as pd

# class Mult:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def __repr__(self):
#         return f'{self.x}x{self.y}'
#     def getcolor(self):
#         a = multiplication_check(self.x,self.y, False)+multiplication_check(self.x,self.y, True)
#
#         color = ('red',    # красным отмечены пары где не работает "схема мудреца"
#                  'blue',   # синим отмечены пары где необходима проверка на разделитель 0 внутри
#                  'green')  # "схема мудреца" работает без проверки на разделитель 0
#         return 'color: %s' % color[a]

# d = [[Mult(i,j) for j in range(10,100)] for i in range(10,100)]
# df = pd.DataFrame(d,index=range(10,100),columns=range(10,100))
#
# with open('wisdom_multiplication_table.html','w') as f:
#     f.write(df.style.applymap(lambda v: v.getcolor()).render())


# 4.4 Число Капрекара
# 65='A' .. 90='Z'
# 30='0' .. 39='9'
# def convert(num, to_base=10, from_base=10):
#     num = int(str(num),base=from_base)
#     if not num:
#         return '0'
#     res = ''
#     while num:
#         d = num % to_base
#         res += d < 10 and str(d) or chr(d+55)
#         num //= to_base
#     return res[::-1]
#
# def kaprekar(n, base=10):
#     k = base!=10 and int(convert(n,from_base=base)) or int(n)
#     s = list(convert(str(k**2), base))
#     f = lambda t: convert(''.join(t),from_base=base)
#     # for i in range(1,len(s)):
#     #     a = int(f(s[:i]))
#     #     b = int(f(s[i:]))
#     #     summ = convert(a+b,base)
#     #     if summ == n:
#     #         return True
#     return any(filter(lambda i:int(f(s[i:]))>0 and convert(int(f(s[:i]))+int(f(s[i:])),base)==n, range(1,len(s))))
#
# print(kaprekar('9'))


# def kaprekar(n):
#     s = list(str(n**2))
#     return filter(lambda i:int(''.join(s[i:]))>0 and int(''.join(s[:i]))+int(''.join(s[i:]))==n, range(1,len(s)))
#
# print(kaprekar(218400870420))

# 4.3 Последовательность Люка
# from decimal import *
# getcontext().prec = 50
#
# def fi(L0, L1, n):
#     while n-1:
#         L0, L1 = L1, L0+L1
#         n -= 1
#     return L1/Decimal(L0)
#
# # print(fi(0, 1, 10))
#
# def luka(L0, L1, n):
#     while n:
#         L0, L1 = L1, L0+L1
#         n -= 1
#     return L0
#
# L = lambda n: luka(2,1,n)
# L2n = lambda n: L(n//2)**2 - 2 * (-1)**n
# def L3n(n):
#     tmp = L(n//3)
#     return tmp**3 - 3 * (-1)**n * tmp
#
# def L4n(n):
#     tmp = L(n//4)
#     return tmp**4 - 4 * (-1)**n * tmp**2 + 2
#
# def L5n(n):
#     tmp = L(n//5)
#     return tmp**5 - 5 * (-1)**n * tmp**3 + 5 * tmp
#
# def L6n(n):
#     tmp = L(n//6)
#     return tmp**6 - 6 * (-1)**n * tmp**4 + 9 * tmp**2 - 2 * (-1)**n
#
# def super_L(n):
#     if n > 6 and not n % 6:
#         return L6n(n)
#     if n > 5 and not n % 5:
#         return L5n(n)
#     if n > 4 and not n % 4:
#         return L4n(n)
#     if n > 3 and not n % 3:
#         return L3n(n)
#     if n > 2 and not n % 2:
#         return L2n(n)
#     return L(n)
#
# n = 12
# print(super_L(n))

#
# def fib(q: int) -> int:
#     """ Effective Fibonacci function """
#     return pow(2 << q, q + 1, (4 << 2 * q) - (2 << q) - 1) % (2 << q)

# def luka(L0, L1, n):
#     if n:
#         return luka(L1, L0+L1, n-1)
#     return L0


# 4.2 Постоянная Капрекара
# def numerics(n):
#     return list(map(int, list(str(n))))
#
# def kaprekar_check(n):
#     lst = numerics(n)
#     a = 2 < len(lst) < 7
#     b = n not in [100, 1000, 100000]
#     c = any(map(lambda x: x != lst[0], lst[1:]))
#     return a and b and c
#
# def kaprekar_step(L):
#     f = lambda rev: int(''.join(map(str,sorted(L,reverse=rev))))
#     return abs(f(True) - f(False))
#
#
# def kaprekar_loop_v1(n):
#     if n > 1000:
#         if any(map(lambda x: x != str(n)[0], str(n)[1:])):
#             print(n)
#             if n == 6174:
#                 return n
#             return kaprekar_loop_v1(kaprekar_step(numerics(n)))
#         print(f"Ошибка! На вход подано число {n} - все цифры одинаковые")
#     else:
#         print("Ошибка! На вход подано число 1000")
#
#
# def kaprekar_loop_v2(n):
#     if kaprekar_check(n):
#         prev_numb = set()
#         while n not in (495, 6174, 549945, 631764):
#             if n in prev_numb:
#                 print(f"Следующее число - {n}, кажется процесс зациклился...")
#                 return
#             print(n)
#             prev_numb.add(n)
#             n = kaprekar_step(numerics(n))
#         print(n)
#     else:
#         print(f"Ошибка! На вход подано число {n}, не удовлетворяющее условиям процесса Капрекара")

