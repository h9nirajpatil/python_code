# covert tuple to list

tuple1=(10,20,30)
print(tuple1)

mylist=list(tuple1)  # covert tuple to list
print(mylist)
mylist[0]=99    #updated
print(mylist)

# coverting list to tuple
mytuple=tuple(mylist)
print(mytuple)