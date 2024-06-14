class circle:

    radius=2.1
    pi=3.14

    def area(self):
        return self.pi*self.radius*self.radius

    def cicum(self):
        return 2*self.pi*self.radius

    def dia(self):
        return 2*self.radius

c=circle()

print("The area of circle is:",c.area())
print("The area circumference is:",c.cicum())
print("The diameter is:",c.dia())





