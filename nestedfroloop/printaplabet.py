print("------pattern3-------")
ch=65
for i in range(1,4,1):   #rows
    for j in range(1,4,1):   #colms
        value=chr(ch)    #covert the integer to character
        print(value,end=" ")
        ch+=1
    print()   #it takes the cursor to the next row