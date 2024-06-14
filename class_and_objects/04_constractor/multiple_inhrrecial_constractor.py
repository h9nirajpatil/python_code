class School:

    school_name=''

    def  __init__(self,school_name):
        self.school_name=school_name

class College:

    college_name=''

    def __init__(self,college_name):
        self.college_name=college_name

class Student(School,College):

    name=''
    roll_no=0

    def __init__(self,name,rollno,school_name,college_name):
        School.__init__(self,school_name)
        College.__init__(self,college_name)

        self.name=name
        self.roll_no=rollno

    def display(self):
        print("---------------- STUDENT DETAILS-------------------")
        print("\t\tStudent Name:",self.name)
        print("\t\tStudent Roll_no:", self.roll_no)
        print("\t\tSchool Name:", self.school_name)
        print("\t\tCollege Name:", self.college_name)

sd=Student('niraj',20,'k r','d y')
sd.display()



