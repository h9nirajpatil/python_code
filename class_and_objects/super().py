class Animal:

    color='black'

    def msg(self):
        print("hello")

class Dog(Animal):

    color = 'white'

    def msg(self):
        print("bye")

    def printColor(self):
        print(self.color)
        print(super().color)
        self.msg()
        super().msg()

obj=Dog()
obj.printColor()