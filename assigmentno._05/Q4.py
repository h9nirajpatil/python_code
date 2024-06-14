class Balancewithrange(Exception):
    pass

class Bank:
    def amountcheck(self):
        AMT = int(input("Enter The Amount:"))
        if(AMT<=10000):
            raise Balancewithrange("Balance is not with in range... please maintain the amount..")

        else:
            print("your account balance is maintained.....")

a=Bank()
try:
    a.amountcheck()
except Balancewithrange as e:
    print(e)