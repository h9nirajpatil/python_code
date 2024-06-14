
#1st creating empty list for store values in list
list=[]
#asking list range
n=int(input("Enter  the values you want in the list:-"))
#condition
for i in range(0,n):
    user= int(input("Enter  the  elements:-"))

    list.append(user) #user adding the list element

    print(list)