print("Enter Marks Obtained in 5 Subjects: ")
markOne = int(input("Enter English Marks:"))
markTwo = int(input("Enter Maths Marks:"))
markThree = int(input("Enter Science Marks:"))
markFour = int(input("Enter So-Science Marks:"))
markFive = int(input("Enter IT Marks:"))

tot = markOne+markTwo+markThree+markFour+markFive
avg = tot/5

if avg>=0 and avg<=50:
    print("Your Failed Exam")
elif avg>=50 and avg<75:
    print("Your completed  1st Class")
elif avg>=75 and avg<100:
    print("Your completed Distinction")

