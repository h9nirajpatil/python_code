# n=int(input("Enter a number:"))
# tot=0
# while(n>0):
#     dig=n%10
#     tot=tot+dig
#     n=n//10
# print("The total sum of digits is:",tot)

# substaction of digit given by the user
# n=int(input("Enter a number:"))
# tot=0
# while(n>0):
#     dig=n%10
#     tot=tot-dig
#     n=n//10
# print("The total sum of digits is:",tot)


num1=int(input("Enter the 1st number:"))
num2=int(input("Enter the 2st number:"))

print("number one is printed",num1)
print("number two is printed",num2)

temp=num1
num1=num2
num2=temp

print("number one after swapping is printed",num1)
print("number two after swapping is printed",num2)

