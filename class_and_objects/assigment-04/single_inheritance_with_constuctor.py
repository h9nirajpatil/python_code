class Student:

    rollno=0
    name=''

    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name

class Marks(Student):

    grade=''

    def __init__(self,rollno,name,grade):
        super().__init__(rollno,name)
        self.grade=grade

    def display(self):
        print("********* Student Details *******")
        print("Student Rollno:",self.rollno)
        print("Student Name:", self.name)
        print("Student Marks:", self.grade)
        print("_________________________________")

r=input("Enter the rollno:")
n=input("Enter the name:")
m=input("Enter the marks:")

mar=Marks(r,n,m)
mar.display()


