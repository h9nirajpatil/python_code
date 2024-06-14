# creating tow tuple and concate the
tuple1=(11,22,33,44,'aaa',444,'bbbb',555)
tuple2=(66,77,88,'ccc','john')
total_tuple=tuple1+tuple1
print(total_tuple)
# print the number of values / size in thetuples
print(("Size of the tuples:-",len(total_tuple)))
#to check whether values is present or not
print("to check value is present or not", 10 in total_tuple)
#to repeat values
t1=(11,2,3,[3]*3,5,'aa')
print(t1)
#print using loop
for i in total_tuple:
    print(i,end="")