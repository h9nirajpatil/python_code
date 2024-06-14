class Employee:

    empId=0
    eName=''
    salary=0

    def __init__(self,empId,eName,salary):
        self.empId = empId
        self.eName = eName
        self.salary = salary

    def dispplay(self):
        print("***** Employee Details")
        print("Employee ID IS:-",self.empId)
        print("Employee Name IS:-:-",self.eName)
        print("Employee Salary IS",self.salary)
        print("----------------------------------------")

    def totalslremp(self,allowance):
        self.salary += allowance
        print("Total Salary Of Employee Is:-",self.salary)
        print("----------------------------------------")

class manager(Employee):

    noofprojects=0

    def __init__(self,empId,eName,salary,noofprojects):
        super().__init__(empId,eName,salary)
        self.noofprojects = noofprojects

    def totalman(self,bonus):
        super().dispplay()
        self.salary =self.salary + (bonus * noofprojects)
        print("Total salary of manager is",self.salary)


class hr(Employee):

    noofrecrument=0

    def __init__(self,empId,eName,salary,noofrecrument):
        super().__init__(empId,eName,salary)
        self.noofrecrument = noofrecrument

    def totalhr(self,incen):
        super().dispplay()
        self.salary = self.salary  + (incen*self.noofrecrument)
        print("Total salary of manager is", self.salary)






e=Employee(111,'niraj',3500)
e.dispplay()
e.totalslremp(500)


m=manager(222,'girish',2000)
m.totalman(500)


h=hr(333,'prasad',5000)
h.totalhr()














