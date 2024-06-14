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


class Sports(Marks):

    score=0

    def inputscore(self):
        self.score = int(input("Enter the score:-"))

    def display(self):
        print(self.name, " ", self.age, " ", self.grade," ",self.score)


sp=Sports()
sp.inputStudent()
sp.inputGrade()
sp.inputscore()
sp.display()