print("+ADD\n","-sub\n","*mul","/div")
num1=int(input("Enter the first number"))
num2=int(input("Enter the 2nd number"))

def add():
    return num1+num2

choice=input("Enter the task")

if(choice=='+'):
    print("Addition is",(num1+num2))
elif(choice=='-'):
    print("Substraction is",(num1-num2))
elif(choice=='*'):
    mul=num1*num2
    print("Multiplication is",mul)
elif(choice=='/'):
    div=num1%num2
    print("Division is:-",div)
else:
    print("Enter the valid task")
