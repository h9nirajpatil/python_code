# from threading import Thread
#
# class myThread(Thread):
#
#     def run(self):
#         print("Thread id running")
#
# t1=myThread()
# t1.start()
#
# t2=myThread()
# t2.start()

#
# from threading  import  *
# from time import  sleep
#
# class Number(Thread):
#
#     def run(self):
#         print(current_thread().getName())
#         for i in range(1,11,1):
#             sleep(1)
#             print(i)
#
# t1=Number()
# t1.setName("------1-10 Number Print-------- ")
# t1.start()
# t1.join()
#
# t2=Number()
# t2.start()

from threading import  *
from time import  sleep

class Square(Thread):

    def calsquare(self):
        print(current_thread().getName())
        for i in range(1,11,1):
            sleep(1)
            sq = i ** 2
            print(sq)

    def  run(self):
        self.calsquare()

class Cube(Thread):

    def calCube(self):
        print(current_thread().getName())
        for i in range(1,11,1):
            sleep(1)
            cb = i ** 3
            print(cb)

    def run(self):
        self.calCube()


squ=Square()
squ.setName("******* SQUARE ********")
squ.start()
squ.join()

cbe=Cube()
cbe.setName("****** CUBE ***********")
cbe.start()






