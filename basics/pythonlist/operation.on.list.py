#######################Operation On List#########################


list1=[111,222,333,'python','java']
print(list1)

list2=[30,40,888,'c','c++']
print(list2)

#Merge the list

mylist=list1+list2
print(mylist)


#To find Length

print("Length of the list:",len(mylist))

#To see present or not

print("To check wether a valur is present or not:-",'java' in mylist)

#To repeate a value multiple times * (replication operator)

mylist3=[[100]*4,22,33,['niraj']*2]
print(mylist3)

#Print the list using for loop

# for variable in sequence:

for i in mylist:
    print(i)



