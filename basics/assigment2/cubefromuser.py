n = int(input("Enter the value of n:-"))
sum = 0
for value in range(1,n+1):
    cube = value**3
    print(cube)

    sum+=cube
print('sum is',sum)
