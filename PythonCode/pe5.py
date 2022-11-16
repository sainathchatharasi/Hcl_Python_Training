import pandas as pd

df = pd.read_csv('retail.csv')
df.head()

print(df)

df['Line_Price'] = df['Quantity'] * df["UnitPrice"]
df.head()

print(df)