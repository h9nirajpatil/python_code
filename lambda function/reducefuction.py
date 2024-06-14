import functools
lis=[1,3,4,5,6,4,3,2]

#sum of list
print(functools.reduce(lambda a,b: a + b, lis))

#largest element in the list
print(functools.reduce(lambda a,b: a if a > b else b, lis))

#smallest element in the list
print(functools.reduce(lambda a,b: a if a < b else b, lis))