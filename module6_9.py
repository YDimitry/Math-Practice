from operator import mul

import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# 1
#
# torg = pd.read_csv('torg.csv', sep=';', index_col='IE_XML_ID')
# print(torg[['IP_PROP30', 'CP_QUANTITY']].groupby('IP_PROP30').sum().idxmax())
# torg_groupped = torg.groupby(['IP_PROP30'])
# print(torg)
# print(torg_groupped['CP_QUANTITY'].sum().sort_values())

# 2
#
# torg_g = torg[['IP_PROP32','CP_QUANTITY']].groupby(['IP_PROP32']).sum()
# print(torg_g.sort_values(by='CP_QUANTITY'))

# 3
# ds = pd.read_csv('dataset_345422_8.txt', sep=';', index_col='IE_XML_ID')
# print(ds.groupby(['IP_PROP32','IP_PROP30'],as_index=False)['CR_PRICE_1_USD'].sum())
# pinkXL = ds[(ds['IP_PROP30'] == 'pink') & (ds['IP_PROP32'] == 'XL')]
# print(pinkXL.CP_QUANTITY.mul(pinkXL.CR_PRICE_1_USD).sum())

# 4
# ds = pd.read_csv('StudentsPerformance.csv')
# print(ds.groupby(['gender','race/ethnicity']).aggregate({'reading score': 'median'}).max())

# 5
# 1 вариант
# ds['mean'] = ds[['math score','reading score','writing score']].mean(axis=1)
# fe = ds[ds['gender'] == 'female'].groupby(['parental level of education']).mean()['mean'].idxmax()
# print(ds[ds['gender'] == 'male'].groupby(['parental level of education']).mean().loc[fe,'mean'].round(1))
# 2 вариант
# meanScore = ds.groupby(['gender', 'parental level of education']).mean().mean(axis=1)
# print(meanScore.loc[('male',meanScore.loc['female'].idxmax())].round(1))

# 6
# Посчитайте среднюю и медианную зарплату "Wage" футболистов из разных клубов "Club".
# В скольких клубах средняя и медианная зарплаты совпадают?

# ds = pd.read_csv('football_players.csv')
# print(ds.head())
#
# m = ds.groupby('Club')['Wage'].aggregate(lambda x: x.mean() == x.median()).sum()
# print(m)

# 7
# Посчитайте среднюю посещаемость каждой велодорожки отдельно по дням недели.
# Какой день недели (в среднем) наиболее посещаем?

# days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# ds = pd.read_csv('dataset_345422_14.txt',parse_dates=['Date'])
# ds['Day'] = ds['Date'].dt.dayofweek.apply(lambda x:days[x])
# print(ds.groupby('Day').aggregate(['mean']).sum(axis=1))
# print(ds.groupby('Day').aggregate(['mean']).sum(axis=1).idxmax())


# 8
# Посчитайте количество организаций (CompanyID), у которых суммарный объем файлов (FileSize)
# хотя бы одного проекта (ProjectID) превышает средний объем файлов по всем проектам.

# ds = pd.read_csv('dataset_file_storage.csv', sep=';')
# meanProjSize = ds.groupby(['ProjectID'])['FileSize'].sum().mean()
# m = ds.groupby(['CompanyID','ProjectID'])['FileSize'].aggregate(lambda x: x.sum()>meanProjSize)
# print(m.groupby(['CompanyID']).aggregate(any).sum())

# 6.10
#
# orders = pd.read_csv('orders.csv', sep=';', index_col='Order ID')
# products = pd.read_csv('Products.csv', sep=';', index_col='Product_ID')
#
# merged = pd.merge(orders, products, how='inner', left_on='ID товара', right_on='Product_ID')
# socks = merged.loc[merged['Name'].str.contains('Носки') & (merged['Оплачен'] == 'Да')]
# print(socks['Количество'].mul(socks['Price']).sum())
