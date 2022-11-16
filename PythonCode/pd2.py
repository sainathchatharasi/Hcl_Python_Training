import pandas as pd

s = pd.Series([-3,5,7,8], index=['a','b','c','d'])
print(s)

ser = pd.Series(s, index=[10,11,12,13,14])
print(ser)