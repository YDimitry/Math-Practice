from operator import mul

import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# 1
#
torg = pd.read_csv('torg.csv', sep=';', index_col='IE_XML_ID')
# print(torg[['IP_PROP30', 'CP_QUANTITY']].groupby('IP_PROP30').sum().idxmax())
# torg_groupped = torg.groupby(['IP_PROP30'])
print(torg)
# print(torg_groupped['CP_QUANTITY'].sum().sort_values())

# 2
#
torg_g = torg[['IP_PROP32','CP_QUANTITY']].groupby(['IP_PROP32']).sum()
print(torg_g.sort_values(by='CP_QUANTITY'))


# 6.10
#

#
# orders = pd.read_csv('orders.csv', sep=';', index_col='Order ID')
# products = pd.read_csv('Products.csv', sep=';', index_col='Product_ID')
#
# merged = pd.merge(orders, products, how='inner', left_on='ID товара', right_on='Product_ID')
# socks = merged.loc[merged['Name'].str.contains('Носки') & (merged['Оплачен'] == 'Да')]
# print(socks['Количество'].mul(socks['Price']).sum())







































































