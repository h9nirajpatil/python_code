n=int(input("Enter the number of rows:-"))
ch=65
for i in range(0,n):
    for j in range(0,i+1):
        value=chr(ch)
        print(value,end=" ")
        ch+=1
    print()