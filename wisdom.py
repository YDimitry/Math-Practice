# 4.5 Таблица умножения двузначных чисел от "Мудреца"
import pandas as pd


def wisdom_multiplication(x, y, length_check=True):
    """умножение по схеме мудреца. В зависимости от значения аргумента length_check
     проверяет необходимости добавить '0' ко второму числу или нет"""
    a, b = (100 - x), (100 - y)
    chk = lambda x: len(str(x)) < 2 and '0' or ''
    return int(str(100 - (a + b)) + chk(a * b) * length_check + str(a * b))


def multiplication_check(x, y, length_check):
    """проверка правильности работы 'схемы мудреца'"""
    return wisdom_multiplication(x, y, length_check) == x * y


class Pair:
    """класс пары множителей"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{self.x}x{self.y}'

    def getcolor(self):
        """функция возвращает цвет в зависимости от правильности работы 'схемы мудреца'"""
        a = multiplication_check(self.x, self.y, False) + multiplication_check(self.x, self.y, True)

        color = ('red',  # красным отмечены пары где не работает "схема мудреца"
                 'blue',  # синим отмечены пары где необходима проверка на разделитель 0 внутри
                 'green')  # "схема мудреца" работает без проверки на разделитель 0
        return 'color: %s' % color[a]


d = [[Pair(i, j) for j in range(10, 100)] for i in range(10, 100)]
df = pd.DataFrame(d, index=range(10, 100), columns=range(10, 100))
df.style.applymap(lambda v: v.getcolor())

# with open('wisdom_multiplication_table.html', 'w') as f:
#     f.write(df.style.applymap(lambda v: v.getcolor()).render())
