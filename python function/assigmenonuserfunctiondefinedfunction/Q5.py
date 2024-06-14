height=4
breadth=2
def triangle(base):
    return 0.5*base*height
bas=float(input("Enter the base of triangle:-"))
areaoftriangle=triangle(bas)
print("The area of triangle is:-",areaoftriangle)

def reactangle(L,B):
    return L*B
length=float(input("Enter the length of rectangle:-"))
areaofrectangle=reactangle(length,breadth)
print("The area of rectangle is:-",areaofrectangle)

def square(side):
    return side*2
siidee=float(input("Enter the side of square:-"))
areaofsquare=square(siidee)
print("The area of square is:-",areaofsquare)
