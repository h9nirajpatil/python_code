class Person:

    name=''
    age=0

    def inputPerson(self):

        self.name = input("Enter the name:-")
        self.age = int(input("Enter the age:-"))

class Student(Person):

    rollno=0
    marks=0

    def inputStudent(self):

        self.rollno = int(input("Enter the rollno:-"))
        self.marks =int(input("Enter the marks:-"))

    def displayStudent(self):
        print(self.name, " ", self.age, " ", self.rollno," ",self.marks)

class Employee(Person):

    empid=0
    salary=0

    def inputEmployee(self):

        self.empid = int(input("Enter the employee ID:-"))
        self.salary = int(input("Enter the Salary:-"))

    def displayEmployee(self):
            print(self.name, " ", self.age, " ", self.empid, " ", self.salary)

print('------------STUDENT DETAILS-----------')
std=Student()
std.inputPerson()
std.inputStudent()
std.displayStudent()

print('------------EMPLOYEE DETAILS-----------')
std=Employee()
std.inputPerson()
std.inputEmployee()
std.displayEmployee()
