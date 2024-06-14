class Employee:

    name=''
    empid=0
    salary=0

    def __init__(self,name,empid,slaary):
        self.name = name
        self.empid = empid
        self.salary = slaary

    def display(self):
        print(self.name," ",self.empid," ",self.salary)

limit=int(input("Enter no of object you want:-"))
emplist=[]

for i in range(0,limit):
    n= input("Enter  the  name:-")
    e=int(input("Enter empid no:-"))
    s=int(input("Enter the salary:-"))
    obj=Employee(n,e,s)
    emplist.append(obj)

for i in emplist:
    i.display()


