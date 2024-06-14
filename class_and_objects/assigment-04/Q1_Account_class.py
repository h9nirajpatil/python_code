class Account:

    acc_name=''
    acc_no=''
    balance=0

    def __init__(self):
        self.acc_name=input("What is your name? Enter Below Section!\n")
        self.acc_no=int(input("What is you account number? Enter Below Section!\n"))
        self.balance=int(input("Enter your balance!\n"))


    def display(self):
        print("*************  Person  Bank  Details  *************\n")
        print("\tPerson Name:-",self.acc_name,"\n","\tPerson Bank Account Number:-",self.acc_no,"\n","\tBank Balance:-",self.balance)
        print("---------------------------------------------------------------------")

    def hello(self):
        print("Hello!!! Welcome to the Bank Of Baroda\n")

    def deposit(self):
        amount = float(input("\tEnter amount to be Deposited: "))
        self.balance += amount
        print("\n \tAmount after Deposit:", self.balance)
        print("---------------------------------------------------------------------")

    def withdraw(self):
        amount = float(input("\n\tEnter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n \t Amount after withdrawn:", self.balance)
            print("------------------------------------------------------------------")
        else:
            print("\n \tInsufficient balance  ")
            print("-------------------------------------------------------------------")


    def checkbalance(self):
        print("\n \tNet Available Balance=", self.balance)

b=Account()
b.display()
b.hello()
b.deposit()
b.withdraw()
b.checkbalance()