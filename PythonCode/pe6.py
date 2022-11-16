import pandas as pd

df = pd.read_csv('retail.csv')
df.head()

print(df)

df['Line_Price'] = df['Quantity'] * df["UnitPrice"]
df.head()

print(df)

df_customers = df.groupby('CustomerId').agg(
orders = ('Invoice.no','nunique'),
skus = ('stock code','nunique'),
quantity = ('Quantity','sum'),
revenue=('Line_Price','sum'),
).reset_index()

df_customers.head()

print(df_customers)