
class Employee:

    #variable diclaration
    empid=''
    ename=""
    salary=0

    def __init__(self):

        #input from user
        self.empid =int(input("Enter the id:"))
        self.ename=input("Enter the  name:")
        self.salary= int(input("Enter the salary:"))

    def display(self):

        #Details Print
        print("*****************   EMPLOYEE DETAILS    ******************")
        print("Employee ID:",self.empid)
        print("Employee Name: ",self.ename)
        print("Employee Salary:",self.salary)

#making a obj here
obj=Employee()
obj1=Employee()
obj2=Employee()

#Displaying
obj.display()
obj1.display()
obj2.display()

#condition/method
if (obj.salary>obj1.salary and obj.salary>obj2.salary):
    print("\n",obj.ename,"has highest salary of",obj.salary)

elif (obj1.salary>obj.salary and obj1.salary>obj2.salary):
    print("\n",obj1.ename,"has highest salary of",obj1.salary)
else:
    print("\n",obj2.ename, "has highest salary of", obj2.salary)

