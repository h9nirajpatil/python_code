#Create a dictionary
mydata={101:"ABC",102:'DEF',102:"XYZ",'aaa':9000}
print(mydata)

#Access value through dictionary
print(mydata[101])
print(mydata['aaa'])

#Modify a value in a dictionary
mydata[101]='John'
print(mydata)

#add a new item to dictionary
mydata[105]='alice'
print(mydata)

#remove an item from dictionary
del mydata[102]
print(mydata)

# remove an last item  key
mydata.popitem()
print(mydata)

#remove the item using key
mydata.pop('aaa')
print(mydata)

#empty the dictionary
mydata.clear()
print(mydata)

del mydata