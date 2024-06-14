name=input("Enter name:-")
rollno=int(input("Enter rollno:-"))
address=input("Enter address:-")
marks=int(input("Enter the marks:-"))
student=(name,rollno,address,marks)

for i in student:
    print(i)

mylist=list(student)


mylist[3]=int(input('Enter the new marks:-'))
print(mylist)