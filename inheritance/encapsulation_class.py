class bike:
    __speed__=80

    def printSpeed(self):
        print(self.__speed__)

b=bike()
b.speed=100
b.printSpeed()