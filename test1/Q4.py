n = int(input("Enter the value of n:-"))
sum = 0
for value in range(1,n+1):
    sq = value**2
    print(sq)
    sum+=sq
print('sum is',sum)