import pandas as pd

data = {'country':["india","australia","brazil"],'capital':['delhi','melbourne','brasilia'],'population':[27382983,732883929,63738782]}
df = pd.DataFrame(data,columns = ['country','capital','population'])
print(df)
