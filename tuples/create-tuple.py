values=22,11,22,999
print(type(values))
print(values)


mytuple=(10,20,30,'ABC','ppp',99,211,33,'aaa')
print(mytuple)

#Indexing

print(mytuple[0])
print(mytuple[-1])


#Slicing:--- to get the part of the tuple

print(mytuple[0:3])
print(mytuple[-4:-1])
print(mytuple[:-1])  # print all the values except last one
print(mytuple[0:1]) # print all values in the tuples
print(mytuple[0:]) # print the all values in the tuples
print(mytuple[:]) # print the all values in the tuples
print(mytuple[::-1]) # reverse the tuple