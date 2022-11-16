import pandas as pd

df = pd.read_csv('nba.csv',index_col = "Name")
print(df)
first = df[["Age","College","Salary"]]
print(first)