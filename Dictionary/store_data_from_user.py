# Iterate it over the loop
Person_data={}
size=int(input("Enter the value of dictionary:"))

for i in range(0,size+1,1):
    name= input("Enter  the name:-")
    age= int(input("Enter  the age:-"))
    #add item to the dictionary
    Person_data[name]=age
print(Person_data)

for k,v in Person_data.item():
    print(k,"-->",v)
