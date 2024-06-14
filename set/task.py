size=int(input('how many values you want to store in a set:'))
myset=set()
sum=0
for i in range(0,size,1):
    data=int(input('Enter the data:'))
    if(data>0):
        myset.add(data)
        sum=sum+data
print(myset)
print('Sum of data:',sum)