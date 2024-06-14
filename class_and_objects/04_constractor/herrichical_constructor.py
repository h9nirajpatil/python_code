class Person:

    name=''
    age=0

    def __init__(self,name,age):

        self.name = name
        self.age = age

class Student(Person):

    rollno=0
    marks=0

    def __init__(self,name,age,rollno,marks):
        super().__init__(name,age)

        self.rollno = rollno
        self.marks= marks

    def displayStudent(self):
        print(self.name, " ", self.age, " ", self.rollno," ",self.marks)

class Employee(Person):

    empid=0
    salary=0

    def __init__(self,name,age,empid,salary):
        super().__init__(name,age)

        self.empid = empid
        self.salary = salary

    def displayEmployee(self):
            print(self.name, " ", self.age, " ", self.empid, " ", self.salary)

print('------------STUDENT DETAILS-----------')
std=Student('john',12,33,33)
std.displayStudent()

print('------------EMPLOYEE DETAILS-----------')
std=Employee('niraj',23,4,443)
std.displayEmployee()