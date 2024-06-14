num1=int(input("Enter the first number:-"))
num2=int(input("Enter the 2nd number:-"))

def largestno():
    if (num1 > num2):
        largestnumber=num1
        return largestnumber


def smallestno():
    if (num1 < num2):
        smallestnumber = num1
        return smallestnumber


while(True):

    print("1.largestnumber\n","2.smallestnumber\n","3.Exit")

    choice=int(input("Enter the task choice:-"))

    if (choice == 1):
        print("Largest Number is", largestno())

    elif (choice == 2):
        print("Smallest Number is", smallestno())

    elif (choice == 3):
        exit()

    else:
        print("Enter the valid task")