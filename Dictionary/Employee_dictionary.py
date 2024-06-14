
Employee={'Name':'John','Age':29,'Salary':25000,'Company':'GOOGLE'}
print(Employee)

age=int(input("Enter the age:"))
salary=int(input("Enter the salary:"))

Employee.update({'Age': age})
Employee.update({'Salary': salary})
print(Employee)