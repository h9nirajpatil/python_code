################ ----- List Manupulatuion  ------------##########

mylist=[100,200,300,400,'java','python']
print(mylist)

#to replace a new value in the exiting value
mylist[0]=345
print(mylist)

#to add a single value at end of the list
mylist.append('c++')
print(mylist)

#to add a smultiple values at end of the list
mylist.extend([11,22,33])
print(mylist)

#to add a value at any position
mylist.insert(3,333)
print(mylist)

#to remove a value in a list usinng value
mylist.remove(400)
print(mylist)

#to remove a value using index
del mylist[4]
print(mylist)

#To remove more than one values
del  mylist[1:6]
print(mylist)

#to remove last value
mylist.pop()
print(mylist)

#to clear tlist
mylist.clear()
print(mylist)

#to delete list
del mylist
print(mylist)

