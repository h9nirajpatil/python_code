try:#is a block which moght have exception
    div=3/2
    print(div)
    list1=[1,2,3,4]
    list1[7]=90
    print("hii")

except ZeroDivisionError as e:#it will executes only when there is exception#it will terminate only one exception ata time...
    print(e)

except IndexError as e:
    print(e)

else:#it will excutes only whwn there is no exception
 print("When there is no exception")

finally:#it always excutes whether exception occurs or not
    print("Always executes")