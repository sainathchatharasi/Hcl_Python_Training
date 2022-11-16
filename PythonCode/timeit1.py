import timeit

s = "sainth"
ss =""
print(timeit.timeit(setup=s,stmt=ss,number=1000))