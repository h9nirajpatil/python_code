age=int(input("Enter the age:"))

if age<=12:
    ride1=12-age
    print("You should have come after",ride1,"years")
elif age>=65:
    ride2=age-65
    print("You should come before",ride2,"years")
else:
    print("enjoy ride")