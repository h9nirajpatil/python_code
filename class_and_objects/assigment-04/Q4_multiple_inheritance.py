class School:

    school_name=''

    def inputschool(self):
        self.school_name=input("Enter the school name:")

class College:

    college_name=''

    def inputcollege(self):
        self.college_name=input("Enter the college name:")

class Student(School,College):

    name=''
    roll_no=0

    def inputstudent(self):
        self.name=input("Enter the name:")
        self.roll_no=int(input("Enter the roll number:"))

    def display(self):
        print("---------------- STUDENT DETAILS-------------------")
        print("\t\tStudent Name:",self.name)
        print("\t\tStudent Roll_no:", self.roll_no)
        print("\t\tSchool Name:", self.school_name)
        print("\t\tCollege Name:", self.college_name)

sd=Student()
sd.inputschool()
sd.inputcollege()
sd.inputstudent()
sd.display()



