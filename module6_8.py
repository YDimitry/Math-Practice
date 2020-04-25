import pandas as pd
import numpy as np

# задаяа 11
df = pd.DataFrame({'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
                   'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
                   'name': ['Murzik', 'Pushok', 'Kaa', 'Bobik', 'Strelka', 'Vaska', 'Kaa2', 'Murka', 'Graf', 'Muhtar'],
                   'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                   'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']},
                 index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])

# filter_names = ["animal", "age"]
# filter_values = ["cat", 3]

# print(df[(df[filter_names[0]]==filter_values[0])&(df[filter_names[1]]<filter_values[1])])

# задаяа 12
# age_between = [2, 4]
# print(df[df['age'].between(*age_between)])
# print()
# print(df[(df['age']>=age_between[0])&(df['age']<=age_between[1])])

# задаяа 13.1
# index = 'f'
# df['age']['f'] = 1
# df.loc[index,'age'] += 1
# print(df)

# задаяа 13.2
# df.loc[:,'age'] += 1
# print(df)

# задаяа 14.1
# print(df['age'].sum())
# print(sum(df['age'][df['age'].notnull()]))

# задаяа 14.2

# df = pd.DataFrame({'name' : ["Alex", "Bob", "Carmen", "Diaz", "Ella","Forman", "Glen"],
#                    'age' : [20, 27, 35, 55, 18, 21, 35],
#                    'designation': ["VP", "CEO", "CFO", "VP", "VP", "CEO", "MD"]})

# for k, v in df.iteritems():
#     if v.values.dtype.name in ['float64', 'int64']:
#         print(f'{k}:{v.sum()}')

# задаяа 15
# df = pd.DataFrame({'name' : ["Alex", "Bob", "Carmen", "Diaz", "Ella","Forman", "Glen"],
#                    'age' : [20, 27, 35, 55, 18, 21, 35],
#                    'designation': ["VP", "CEO", "CFO", "VP", "VP", "CEO", "MD"]})
# group_by = "designation"
#
# print(df.groupby([group_by]).mean()['age'])


# задаяа 16
# new_index = "k"
# new_data = [5.5, "dog", "Belka", "no", 2]
# del_index = "f"
# df.loc[new_index] = new_data
# df = df.drop(del_index)
# print(df)

# задаяа 17
# group_by = "animal"
# df = pd.DataFrame({'name' : ["Alex", "Bob", "Carmen", "Diaz", "Ella","Forman"],
#                    'age' : [20, 27, 35, 55, 18, 21],
#                    'designation': ["VP", "CEO", "CFO", "VP", "VP", "CEO"]})
# group_by = "designation"
# print(df[group_by].value_counts())


# задаяа 18
# sort_by = ["age", "visits"]
# print(df.sort_values(sort_by,ascending=[False, True]))

# задаяа 19
# column = "priority"
# df = pd.DataFrame({'name' : ["Alex", "Bob", "Carmen", "Diaz", "Ella","Forman", "Glen"],
#                    'age' : [20, 27, 35, 55, 18, 21, 35],
#                    'on vacation': [1, 1, 0, 0, 0, 1, 0],
#                    'designation': ["VP", "CEO", "CFO", "VP", "VP", "CEO", "MD"]})
# column = "on vacation"

# df.loc[:,column] = df[column].map(lambda x: x in ('yes', 1))
# df.loc[:,column] = df[column].apply(lambda x: x in ('yes', 1))
# print(df)

# задаяа 20
# column = 'animal'
# old_value = 'snake'
# new_value = 'python'
#
# df = df.replace({column:old_value},new_value)
# print(df)









































