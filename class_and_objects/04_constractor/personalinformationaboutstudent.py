class Student:
    name=''
    rollno=0
    marks=0
    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def display(self):
        print(self.name," ",self.rollno," ",self.marks)

obj=Student("niraj",20,80)
obj1=Student("girish",19,90)
obj2=Student("prasad",22,100)



obj.display()  # they are also known as reference variable
obj1.display()
obj2.display()

if (obj.marks>obj1.marks and obj.marks>obj2.marks):
    print(obj.name,"has highest marks of",obj.marks)

elif (obj1.marks>obj.marks and obj1.marks>obj2.marks):
    print(obj1.name,"has highest marks of",obj1.marks)
else:
    print(obj2.name, "has highest marks of", obj2.marks)







