#empty set
# myset=set()
# print(type(myset))

myset={10,20,30,10,10,'john'}#it allows ony unique values
print(myset)

#add only one values at a time
myset.add(700)
print(myset)

myset.add('niraj')
print(myset)

myset.update([10,2,39])#dd more than one values
print(myset)

#to remove from the set
# myset.remove(11)#if unknown values is given an error
# print(myset)

myset.discard(11322)
print(myset)

myset.pop()#remove first value
print(myset)

myset.clear()
print(myset)

