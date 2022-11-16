import multiprocessing
import time
import pdb

class Process(multiprocessing.Process):
    def __init__(self,id):
        super(Process, self).__init__()
        self.id = id

    def run(self):
        time.sleep(1)
        print("i'm the process with id: {}".format(self.id))

pdb.trace()
if __name__ == "__main__":
    p = Process(0)

    #create a new process and invoke the process.run() method
    p.start()

    #process.join() to wait for task completion
    p.join()
    p = Process(1)
    p.start()
    p.join()
