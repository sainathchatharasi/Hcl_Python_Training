import multiprocessing
import time

def square(x):
    return x * x

if __name__ == '__main__':

    #multiprocessing pool object
    pool = multiprocessing.Pool()

    #pool object with number of element
    pool = multiprocessing.Pool(processes=2)

    inputs = [0,1,2,3,4]

    outputs = pool.map(square, inputs)

    print("inputs : ",inputs)
    print("outputs :",outputs)
    print(time.time())
