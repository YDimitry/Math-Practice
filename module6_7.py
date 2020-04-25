# задача 1
import pandas as pd
import numpy as np
# задача 2
# print(pd.__version__)
# print(pd.show_versions())

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# задача 4
df = pd.DataFrame(data, labels)
# print(df)

# col = "animal"
# row = "e"
# print(df[col][row])

# задача 5
# descr = df.describe()
# print(descr['age']['count'])
# print(descr['age']['75%'])

# задача 6.1
# print(df[:3])

# задача 6.2
# print(df.iloc[[0,2,3]])

# задача 7
df = pd.DataFrame({'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
                   'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
                   'name': ['Murzik', 'Pushok', 'Kaa', 'Bobik', 'Strelka', 'Vaska', 'Kaa2', 'Murka', 'Graf', 'Muhtar'],
                   'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                   'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']},
                 index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])

# print(df[['name','age']])
# задача 8
# print(df[['name','age']].iloc[[0,2,3]])

# задача 9
# critical_age = 3
# print(df[df['age']>critical_age])

# задача 10
print(df[np.isnan(df['age'])])

























































