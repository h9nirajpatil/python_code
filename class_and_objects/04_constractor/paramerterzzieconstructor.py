class Person:
    name=''
    age=0

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name," ",self.age)

obj=Person("John",21)
obj.display()