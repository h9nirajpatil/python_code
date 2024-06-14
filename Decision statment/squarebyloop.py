limit = int(input("Enter number:-"))
sum=0
for i in range(1,limit+1,1):
        sq=i*i
        print(sq,end=",")
        sum+=sq
print("\nSum of square:-",sum)
