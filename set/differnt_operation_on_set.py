A={10,20,30,40}
B={20,30,80,90,100}
print(A.union(B))

#or
print(A|B)#using symbols
print(A.intersection(B))
print(A&B)

print(A.difference(B))
print(A-B)

print(B.difference(A))
print(B-A)

#copy()  is used to get the copy of values in the set
copySet=A.copy()
print(copySet)

copySet.add(3000)
print(copySet)
print(A)

# min() max() sum()

nums={10,20,30}
print("Largest no.",max(nums))
print("Smallest no.",min(nums))
print("Sum of number",sum(nums))