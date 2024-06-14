# from threading import Thread
#
# class myThread(Thread):
#
#     def run(self) :
#         print("Thread id running")
#
# t1=myThread()
# t1.start()
#
# t2=myThread()
# t2.start()


# from threading import *
# from time import sleep
# class Numbers(Thread):
#
#     def run(self):
#         print(current_thread().getName())
#         for i in range(1,11,1):
#             sleep(i)
#             print(i)
#
# t1=Numbers()
# t1.setName("-------abc-----")
# t1.start()
# t1.join() #to lock the thread so that it can complete the task and go
# #to another thread
# t2=Numbers()
# t2.setName("-----xyz--------")
# t2.start()

#
# from threading import *
# from time import sleep
# class square(Thread):
#
#     def calSquare(self):
#         print(current_thread().getName())
#         for i in range(1, 11, 1):
#             sleep(1)
#             sq = i ** 2
#             print(sq)
#
#     def run(self):
#         self.calSquare()
#
# class cube(Thread):
#
#     def calCube(self):
#         print(current_thread().getName())
#         for i in range(1,11,1):
#             sleep(1)
#             cube=i**3
#             print(cube)
#
#     def run(self):
#         self.calCube()
#
# sq=square()
# sq.setName("******SQUARE******")
# sq.start()
# sq.join()
#
# cb=cube()
# cb.setName("******CUBE*****")
# cb.start()
# cb.join()

from threading import *
from time import sleep

class numberfive(Thread):

    def tablefive(self):
        self.num=5
        print(current_thread().getName())
        for i in range(1,11,1):
            sleep(1)
            tblfive= i * self.num
            print(self.num,"X",i,"=",tblfive)

    def run(self):
        self.tablefive()

class numbersix(Thread):

    def tablesix(self):
        self.num1=6
        print(current_thread().getName())
        for i in range(1,11,1):
            sleep(1)
            tblsix= i * self.num1
            print(self.num1,"X",i,"=",tblsix)

    def run(self):
        self.tablesix()

tfiv=numberfive()
tfiv.setName("******* MULTIPLICATION OF TABLE FIVE **************")
tfiv.start()
tfiv.join()

tsix=numbersix()
tsix.setName("******* MULTIPLICATION OF TABLE SIX **************")
tsix.start()

