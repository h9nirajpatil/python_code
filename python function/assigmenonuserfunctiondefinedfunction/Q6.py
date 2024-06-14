maximum = int(input(" Please Enter the Maximum Value : "))
def evenfunction():
    total = 0
    for number in range(1, maximum + 1):
        if (number % 2 == 0):
         print(number,end=" ")
         total =total + number
    return total
evenno=evenfunction()
print("\nThe Sum of Even Numbers is",evenno)

def oddfunction():
    total = 0
    for number in range(1, maximum + 1):
        if (number % 2 == 1):
         print(number,end=" ")
         total =total + number
    return total
oddnumber=oddfunction()
print("\nThe Sum of Odd Numbers is",oddnumber)
