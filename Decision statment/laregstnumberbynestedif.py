num1 = int(input('Enter first number  : '))
num2 = int(input('Enter second number : '))
num3 = int(input('Enter third number  : '))

if (num1>num2):
    if (num1>num3):
        print(num1,"is largest number")
    else:
        print(num3,"is largest number")
else:
    if (num2>num3):
        print(num2,"is largest number")
    else:
        print(num3,"is largest number")