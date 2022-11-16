# import pdb
# pdb.set_trace()
a = 20
b = 10

s = 0

for i in range(a):
    #this line will raise zerodivision error
    a += a/b
    b -=1
