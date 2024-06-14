
def squarelist():
    mylist=[]
    limit=int(input("How many values you want in the list:"))
    for i in range(0, limit):
        user = int(input("Enter  the  elements:-"))
        mylist.append(user)
    print(mylist)

    square_list=list(map(lambda n:n**2,mylist))
    print(square_list)
squarelist()






