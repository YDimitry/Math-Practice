import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

orders = pd.read_csv('orders.csv', sep=';', index_col='Order ID')
products = pd.read_csv('Products.csv', sep=';', index_col='Product_ID')

merged = pd.merge(orders, products, how='inner', left_on='ID товара', right_on='Product_ID')
socks = merged.loc[merged['Name'].str.contains('Носки') & (merged['Оплачен'] == 'Да'),'Price'].sum()

print(socks)

print(merged)






































































