# num1=int(input("ENTER THE NUMBER1:"))
# num2=int(input("ENTER THE NUMBER2:"))
#
# def add():
#     ADD=num1+num2
#     return ADD
# result=add()
#
#
# def sub():
#     SUB=num1-num2
#     return SUB
# result2=sub()
#
#
# def mul():
#     MUL=num1+num2
#     return MUL
# result3=mul()
#
#
# def div():
#     DIV=num1/num2
#     return DIV
# result4=div()
#
# print("+ADD\n","-sub\n","*mul","/div")
#
# choice=input("Enter the task:")
#
# if(choice=='+'):
#     print("Addition is",result)
#
# elif(choice=='-'):
#     print("Substraction is",result2)
#
# elif(choice=='*'):
#     mul=num1*num2
#     print("Multiplication is",result3)
#
# elif(choice=='/'):
#     div=num1/num2
#     print("Division is:-",result4)
#
# else:
#     print("Enter the valid task")


num1=int(input("Enter the first number:-"))
num2=int(input("Enter the 2nd number:-"))

def add():
    return num1+num2

def sub():
    return num1-num2

def mul():
    return num1*num2

def div():
    return num1/num2

def remainder():
    return num1%num2


while(True):

    print("1.ADD\n","2.sub\n","3.mul\n","4.div\n","5.REM\n","6.EXIT")

    choice=input("Enter the task number:-")

    if(choice==1):
        print("Addition is",add())

    elif(choice==2):
        print("Substraction is",sub())

    elif(choice==3):

        print("Multiplication is",mul())
    elif(choice==4):

        print("Division is:-",div())
    elif (choice==5):

        print("Remainder of two nos. is:-", remainder())

    elif (choice==6):

        exit()

    else:
        print("Enter the valid task")