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

class Sports(Marks):

    score=0

    def __init__(self,rollno,name,grade,score):
        super().__init__(rollno,name,grade)
        self.score=score

    def display(self):
        print("********* Student Details *******")
        print("Student Rollno:",self.rollno)
        print("Student Name:", self.name)
        print("Student Marks:", self.grade)
        print("Student Score:", self.score)
        print("_________________________________")

r=input("Enter the rollno:")
n=input("Enter the name:")
m=input("Enter the marks:")
s=int(input("Enter the score:"))

mar=Sports(r,n,m,s)
mar.display()
