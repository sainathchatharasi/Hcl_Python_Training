import pandas as pd

data = pd.read_excel("Companies.xlsx")
df=pd.DataFrame(data,columns='CEO')

print(df)