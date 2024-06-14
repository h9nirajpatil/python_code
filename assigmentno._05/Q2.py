from abc import  ABC,abstractmethod

class GeneralBank(ABC):

    @abstractmethod
    def getsavingInterestRate(self):
        pass

    @abstractmethod
    def getfixedInterestRate(self):
        pass

class ICICI(GeneralBank):

    def getsavingInterestRate(self):
        saving=int(input("Enter the Saving amount"))
        return 0.4 * saving

    def getfixedInterestRate(self):
        fixed=int(input("Enter the Fix amount"))
        return  0.085 * fixed

icic=ICICI()
print("Rate of interest for saving amount is",icic.getsavingInterestRate())
print("Rate of interest for fixed amount is",icic.getfixedInterestRate())


class kotakmahendra(GeneralBank):

    def getsavingInterestRate(self):
        saving = int(input("Enter the Saving amount"))
        return 0.06 * saving

    def getfixedInterestRate(self):
        fixed = int(input("Enter the Fix amount"))
        return 0.09 * fixed

KOTAK=kotakmahendra()
print("Rate of interest for saving amount is",icic.getsavingInterestRate())
print("Rate of interest for fixed amount is",icic.getfixedInterestRate())