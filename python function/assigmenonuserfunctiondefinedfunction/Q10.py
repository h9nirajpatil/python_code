list=[]
n=int(input("Enter  the values you want in the list:-"))
for i in range(0, n):
    user = int(input("Enter  the  elements:-"))

    list.append(user)

    print(list)
square_list=[list**2 for list in list ]
print(" Square of list is below :-")
print(square_list)

