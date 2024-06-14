#how to create abbstract claas in python

from abc import  ABC,abstractmethod

class Myclass(ABC):

    @abstractmethod
    def msg(self):
        pass

    @abstractmethod
    def add(self,n1,n2):
        pass

class Child(Myclass):

    def msg(self):
        print("hello")

    def add(self,n1,n2):
        return n1+n2

obj=Child()
obj.msg()
print("sum is",obj.add(4,6))