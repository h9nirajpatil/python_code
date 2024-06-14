
class student:

    name=''
    age=0

    def inputStudent(self):
        self.name = input("Enter the name:-")
        self.age = int(input("Enter the age:-"))

class Marks(student):

    grade=""

    def inputGrade(self):
        self.grade = input("Enter the grade:")

    def display(self):
        print(self.name," ",self.age," ",self.grade)

obj=Marks()
obj.inputStudent()
obj.inputGrade()
obj.display()
