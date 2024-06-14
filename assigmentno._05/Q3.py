class AgeAboveBelow(Exception):
    pass

class Age:
    def validAge(self):
        age = int(input("Enter The Age:"))
        if(age<=12):
            raise AgeAboveBelow("Too young for ride....")
        elif(age>=65):
            raise AgeAboveBelow("Too old for ride...")
        else:
            print("enjaoy the ride...")

a=Age()
try:
    a.validAge()
except AgeAboveBelow as e:
    print(e)
