class Person:

    name=''
    age=0
    city=''

    def inputPerson(self):
        self.name=input("Enter the name:")
        self.age=int(input("Enter the age:"))
        self.city=input("Enter the city:")

    def display(self):
        print(self.name,"",self.age,"",self.city)

p1=Person()
p1.inputPerson()
p1.display()

p2=Person()
p2.inputPerson()
p2.display()







